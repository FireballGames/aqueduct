#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.levelmap
# import d2game.location

# import game
import game.imagelib
import game.terrain
import game.mapobjects

FIELD_SIZE = (30, 22)


class LevelMap(d2game.levelmap.LevelMap):
    def __init__(self, player):
        d2game.levelmap.LevelMap.__init__(self, player)

        game.terrain.load()
        game.mapobjects.load()
        game.mapobjects.load_aqueducts()

        self.xsize, self.ysize = FIELD_SIZE
        self.aqueducts = []
        self.towns = []

    def random_terrain(self):
        return game.terrain.Grass()
        # import random
        # i = random.randrange(0, 100)
        # if i > 90:
        #     return game.terrain.Water()
        # else:
        #     return game.terrain.Grass()

    def generate_tile(self):
        terr = self.random_terrain()
        if terr.empty:
            return terr

        import random
        i = random.randrange(0, 100)
        if i > 95:
            terr.set_object(game.mapobjects.Rock())
        elif i > 90:
            terr.set_object(game.mapobjects.Tree())

        return terr

    def generate_map(self):
        self.locations = [[self.generate_tile() for j in range(self.ysize)] for i in range(self.xsize)]

        import random
        import logging

        town = game.mapobjects.Town()
        x, y = random.randrange(0, 16), random.randrange(0, 16)
        self.locations[x][y].set_object(town)
        logging.debug((x, y))
        self.towns.append(town)

        well = game.mapobjects.Well()
        x, y = random.randrange(0, 12), random.randrange(0, 12)
        logging.debug((x, y))
        for i in range(x, x+3):
            for j in range(y, y+3):
                self.locations[i][j] = game.terrain.Grass()
                self.locations[i][j].watered = True
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

    def get_random_aqueduct(self):
        import random
        data = random.choice(game.mapobjects.aqueducts)
        a = game.mapobjects.Aqueduct(*data)
        import logging
        logging.debug("Getting aqueduct %s", a)
        return a

    def set_aqueduct(self, tile, aqueduct):
        o = tile.set_object(aqueduct)
        import logging
        logging.debug("Setting aqueduct %s", o)
        self.entities.add(o)
        self.aqueducts.append(o)
        return o

    def update_watering(self):
        aqueducts = [a for a in self.aqueducts if a.update_watered(self)]
        import logging
        logging.debug("Aqueducts %s", str(aqueducts))
        for a in aqueducts:
            logging.debug("Found aqueduct %s", str(a))
            a.set_watered(True)
        for t in self.towns:
            logging.debug("Found town %s", str(t))
            t.set_watered(t.update_watered(self))
            
    def wages(self):
        return 1 + len([t for t in self.towns if t.is_watered()]) * 5            