#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.levelmap
import d2game.location
import pygame.sprite
import pygame.image
import pygame.transform
import game


class SpriteLib(pygame.sprite.Sprite):
    watered = False

    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)

        filename = self.lib[id]
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.type_id = id
        self.start_point = (0, 0)


class TerrType(SpriteLib):
    def __init__(self, id):
        import config.resource
        self.lib = config.resource.Tiles
        SpriteLib.__init__(self, id)


class TileType(SpriteLib):
    def __init__(self, id):
        import config.resource
        self.lib = config.resource.Tiles
        SpriteLib.__init__(self, id)


class TownType(SpriteLib):
    def __init__(self, id):
        import config.resource
        self.lib = config.resource.Towns
        SpriteLib.__init__(self, id)


class WellType(SpriteLib):
    watered = True

    def __init__(self, id):
        import config.resource
        self.lib = config.resource.Wells
        SpriteLib.__init__(self, id)


class AqueductType(SpriteLib):
    def __init__(self, id, start_point, rotation):
        import config.resource
        self.lib = config.resource.Aqueducts
        SpriteLib.__init__(self, id)

        self.start_point = start_point
        self.image = pygame.transform.rotate(self.image, rotation)


class Town(d2game.location.ObjectType):
    type_id = 2


class Well(d2game.location.ObjectType):
    type_id = 3


class Aqueduct(d2game.location.ObjectType):
    type_id = 10


class LevelMap(d2game.levelmap.LevelMap):
    def __init__(self, player):
        d2game.levelmap.LevelMap.__init__(self, player)

        self.terrains = [
            TerrType(0),
            TerrType(1),
        ]

        self.tiles = [
            TileType(2),
            TileType(3),
        ]

        self.towns = [
            TownType(0),
        ]

        self.wells = [
            WellType(0),
        ]

        self.aqueducts = [
            AqueductType(0, (0, -1), 0),
            AqueductType(0, (-1, 0), 90),
            AqueductType(1, (0, 0), 0),
            AqueductType(1, (0, 0), 90),
            AqueductType(1, (0, 0), 180),
            AqueductType(1, (0, 0), 270),
        ]

        self.xsize = game.FIELD_SIZE[0]
        self.ysize = game.FIELD_SIZE[1]

    def generate_tile(self):
        import random

        i = random.randrange(0, 100)
        if i > 90:
            return d2game.location.Location(self.terrains[1])
        else:
            terr = self.terrains[0]

        i = random.randrange(0, 100)
        if i > 95:
            return d2game.location.Location(terr, object_type=self.tiles[1])
        elif i > 90:
            return d2game.location.Location(terr, object_type=self.tiles[0])
        else:
            return d2game.location.Location(terr)

    def generate_map(self):
        self.locations = [[self.generate_tile() for j in range(self.ysize)] for i in range(self.xsize)]

        import random
        import logging

        town = Town(self.towns[0])
        x, y = random.randrange(0, 16), random.randrange(0, 16)
        self.locations[x][y].set_object(town)
        logging.debug((x, y))

        well = Well(self.wells[0])
        x, y = random.randrange(0, 12), random.randrange(0, 12)
        logging.debug((x, y))
        for i in range(x, x+4):
            for j in range(y, y+4):
                t = self.locations[i][j]
                t.terrain = self.terrains[0]
                t.image = t.terrain.image
                t.set_object(None)
        self.locations[x][y].set_object(well)

    def generate_surface(self):
        for i in range(self.xsize):
            for j in range(self.ysize):
                tile = self.locations[i][j]
                tile.rect.x = i * 32
                tile.rect.y = j * 32
                self.entities.add(tile)
                if tile.map_object:
                    tile.map_object.rect = tile.rect
                    self.entities.add(tile.map_object)

    def set_random_aqueduct(self, tile):
        import random
        a = random.choice(self.aqueducts)
        o = tile.set_object(a)
        self.entities.add(o)
        return o
