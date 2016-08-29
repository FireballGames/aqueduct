#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.location
import game.imagelib


class TerrType(game.imagelib.SpriteLib):
    def __init__(self, id):
        import config.resource
        self.lib = config.resource.Tiles
        game.imagelib.SpriteLib.__init__(self, self.lib[id])


class Town(d2game.location.MapObject):
    type_id = 2


class Well(d2game.location.MapObject):
    type_id = 3

    def is_watered(self):
        return True


class Aqueduct(d2game.location.MapObject):
    type_id = 10

    def __init__(self, object_type):
        d2game.location.MapObject.__init__(self, object_type)
        self.points = object_type.points

    def get_pos(self):
        return int(self.rect.x / 32), int(self.rect.y / 32)

    def is_watered(self, level):
        import logging
        logging.debug(self.points)
        x, y = self.get_pos()
        logging.debug((x, y))
        l = [level.locations[x + px][y + py] for px, py in self.points]
        w = [i for i in l if i.is_watered()]
        logging.debug(l)
        logging.debug(self.rect)
        logging.debug([i.rect for i in l])
        print(w)
        return len(w) > 0


class Location(d2game.location.Location):
    def __init__(self, terrain, **kargs):
        d2game.location.Location.__init__(self, terrain, **kargs)

        self.watered = False

    def set_object(self, map_object):
        if map_object:
            self.map_object = map_object
            self.map_object.rect = self.rect
            self.map_object.rect.x = self.map_object.rect.x + (self.map_object.start_point[0] * 32)
            self.map_object.rect.y = self.map_object.rect.y + (self.map_object.start_point[1] * 32)
        else:
            self.map_object = None
        return self.map_object

    def is_watered(self):
        if self.map_object and self.map_object.is_watered():
            self.watered = True
        return self.watered
