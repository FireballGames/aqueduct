#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.levelmap
import pygame.sprite
import pygame.image


class TileType(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)

        import config.resource
        filename = config.resource.Tiles[id]
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.type_id = id


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type):
        pygame.sprite.Sprite.__init__(self)
        self.tile_type = tile_type
        self.image = tile_type.image
        self.rect = self.image.get_rect()


class LevelMap(d2game.levelmap.LevelMap):
    def __init__(self, player):
        d2game.levelmap.LevelMap.__init__(self, player)

        self.tiles = {
            0: TileType(0),
            1: TileType(1),
            2: TileType(2),
            3: TileType(3),
        }

    def generate_tile(self):
        import random

        return Tile(self.tiles[0])
        i = random.randrange(0, 100)
        if i > 90:
            return Tile(self.tiles[3])
        elif i > 75:
            return Tile(self.tiles[2])
        elif i > 50:
            return Tile(self.tiles[1])
        else:
            return Tile(self.tiles[0])

    def generate_map(self):
        self.locations = [[self.generate_tile() for j in range(self.ysize)] for i in range(self.xsize)]

    def generate_surface(self):
        for i in range(self.xsize):
            for j in range(self.ysize):
                tile = self.locations[i][j]
                tile.rect.x = i * 32
                tile.rect.y = j * 32
                self.entities.add(tile)
