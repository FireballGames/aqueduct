#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.levelmap
import pygame.sprite
import pygame.image


class TerrType(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)

        import config.resource
        filename = config.resource.Tiles[id]
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.terr_id = id

class TileType(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)

        import config.resource
        filename = config.resource.Tiles[id]
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.type_id = id


class TileObject(pygame.sprite.Sprite):
    def __init__(self, tile_type):
        pygame.sprite.Sprite.__init__(self)
        self.tile_type = tile_type
        self.image = tile_type.image
        self.rect = self.image.get_rect()


class Tile(pygame.sprite.Sprite):
    def __init__(self, terrain, tile_type=None):
        pygame.sprite.Sprite.__init__(self)

        self.terrain = terrain
        self.image = terrain.image
        self.rect = self.image.get_rect()
        if tile_type:
            self.tile_object = TileObject(tile_type)
            self.tile_object.rect = self.rect
        else:
            self.tile_object = None


class LevelMap(d2game.levelmap.LevelMap):
    def __init__(self, player):
        d2game.levelmap.LevelMap.__init__(self, player)

        self.terrains = {
            0: TerrType(0),
            1: TerrType(1),
        }

        self.tiles = {
            0: TileType(2),
            1: TileType(3),
        }

    def generate_tile(self):
        import random

        i = random.randrange(0, 100)
        if i > 90:
            return Tile(self.terrains[1])
        else:
            terr = self.terrains[0]

        i = random.randrange(0, 100)
        if i > 95:
            return Tile(terr, self.tiles[1])
        elif i > 90:
            return Tile(terr, self.tiles[0])
        else:
            return Tile(terr)

    def generate_map(self):
        self.locations = [[self.generate_tile() for j in range(self.ysize)] for i in range(self.xsize)]

    def generate_surface(self):
        for i in range(self.xsize):
            for j in range(self.ysize):
                tile = self.locations[i][j]
                tile.rect.x = i * 32
                tile.rect.y = j * 32
                self.entities.add(tile)
                if tile.tile_object:
                    self.entities.add(tile.tile_object)
