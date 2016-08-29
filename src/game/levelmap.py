#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.levelmap
import d2game.location
import pygame.sprite
import pygame.image
import pygame.transform
import game
import game.imagelib
import game.terrain


class TileType(game.imagelib.SpriteLib):
    watered = False

    def __init__(self, id):
        import config.resource
        self.lib = config.resource.Tiles
        game.imagelib.SpriteLib.__init__(self, self.lib[id])


class TownType(game.imagelib.SpriteLib):
    watered = False

    def __init__(self, id):
        import config.resource
        self.lib = config.resource.Towns
        game.imagelib.SpriteLib.__init__(self, self.lib[id])


class WellType(game.imagelib.SpriteLib):
    watered = True

    def __init__(self, id):
        import config.resource
        self.lib = config.resource.Wells
        game.imagelib.SpriteLib.__init__(self, self.lib[id])


class AqueductType(game.imagelib.SpriteLib):
    def __init__(self, id, rotation, points):
        import config.resource
        self.lib = config.resource.Aqueducts
        game.imagelib.SpriteLib.__init__(self, self.lib[id])

        self.start_point = (0, 0)
        self.points = points
        self.image = pygame.transform.rotate(self.image, rotation)


class LevelMap(d2game.levelmap.LevelMap):
    def __init__(self, player):
        d2game.levelmap.LevelMap.__init__(self, player)

        self.terrains = [
            game.terrain.TerrType(0),
            game.terrain.TerrType(1),
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

        self.aqueduct_types = [
            AqueductType(0, 0, ((0, -1), (0, 1))),
            AqueductType(0, 90, ((-1, 0), (1, 0))),
            AqueductType(1, 0, ((0, -1), (1, 0))),
            AqueductType(1, 90, ((-1, 0), (0, -1))),
            AqueductType(1, 180, ((0, 1), (-1, 0))),
            AqueductType(1, 270, ((1, 0), (0, 1))),
        ]

        self.xsize = game.FIELD_SIZE[0]
        self.ysize = game.FIELD_SIZE[1]
        self.aqueducts = []

    def generate_tile(self):
        import random

        i = random.randrange(0, 100)
        if i > 90:
            return d2game.location.Location(self.terrains[1])
        else:
            terr = self.terrains[0]

        i = random.randrange(0, 100)
        if i > 95:
            return game.terrain.Location(terr, object_type=self.tiles[1])
        elif i > 90:
            return game.terrain.Location(terr, object_type=self.tiles[0])
        else:
            return game.terrain.Location(terr)

    def generate_map(self):
        self.locations = [[self.generate_tile() for j in range(self.ysize)] for i in range(self.xsize)]

        import random
        import logging

        town = game.terrain.Town(self.towns[0])
        x, y = random.randrange(0, 16), random.randrange(0, 16)
        self.locations[x][y].set_object(town)
        logging.debug((x, y))

        well = game.terrain.Well(self.wells[0])
        x, y = random.randrange(0, 12), random.randrange(0, 12)
        logging.debug((x, y))
        for i in range(x, x+3):
            for j in range(y, y+3):
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
        a = random.choice(self.aqueduct_types)
        o = tile.set_object(game.terrain.Aqueduct(a))
        print(o)
        self.entities.add(o)
        self.aqueducts.append(o)
        return o

    def update_watering(self):
        aqueducts = [a for a in self.aqueducts if a.is_watered(self)]
        import logging
        logging.debug(aqueducts)
        for a in aqueducts:
            print(a)
