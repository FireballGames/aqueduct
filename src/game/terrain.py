#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.location
import game.imagelib

GRASS_ID = 0
WATER_ID = 1

resources = dict()


def load():
    global resources
    import config.resource
    resources = {
        GRASS_ID: config.resource.load(config.resource.Tiles, 0),
        WATER_ID: config.resource.load(config.resource.Tiles, 1),
    }
    return resources


class Location(d2game.location.Location):
    type_id = 0
    empty = False

    def __init__(self):
        d2game.location.Location.__init__(self, self.get_image())

        self.watered = False

    def is_watered(self):
        import logging
        logging.debug("Map object is %s", str(self.map_object))

        if self.map_object and self.map_object.is_watered():
            self.watered = True
        return self.watered

    def get_image(self):
        return resources[self.type_id]

    def get_pos(self):
        return int(self.rect.x / 32), int(self.rect.y / 32)

    def can_build(self):
        if self.empty:
            return False
        if self.map_object:
            return not self.map_object.empty
        return True
        
class Water(Location):
    type_id = WATER_ID
    empty = True
    watered = False


class Grass(Location):
    type_id = GRASS_ID
    empty = False
