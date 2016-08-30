#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.location

TREE_ID = 0
ROCK_ID = 1
WELL_ID = 2
TOWN_ID = 3
AQUEDUCT_ID = 4

resources = dict()
aqueducts = []


def load():
    global resources
    import config.resource
    resources = {
        TREE_ID: config.resource.load(config.resource.Tiles, 2),
        ROCK_ID: config.resource.load(config.resource.Tiles, 3),
        TOWN_ID: [
            config.resource.load(config.resource.Towns, 0),
            config.resource.load(config.resource.Towns, 1),
        ],
        WELL_ID: config.resource.load(config.resource.Wells, 0),
        AQUEDUCT_ID: [
            [
                config.resource.load(config.resource.Aqueducts, 0),
                config.resource.load(config.resource.Aqueducts, 1),
            ],
            [
                config.resource.load(config.resource.Aqueducts, 2),
                config.resource.load(config.resource.Aqueducts, 3),
            ],
        ],
    }
    return resources


def load_aqueduct(image_id, points, rotation):
    import pygame.transform
    res = resources[AQUEDUCT_ID][image_id]
    images = [pygame.transform.rotate(image, rotation) for image in res]
    return images, points


def load_aqueducts():
    global aqueducts
    aqueducts = [
        load_aqueduct(0, ((0, -1), (0, 1)), 0),
        load_aqueduct(0, ((-1, 0), (1, 0)), 90),
        load_aqueduct(1, ((0, -1), (1, 0)), 0),
        load_aqueduct(1, ((-1, 0), (0, -1)), 90),
        load_aqueduct(1, ((0, 1), (-1, 0)), 180),
        load_aqueduct(1, ((1, 0), (0, 1)), 270),
    ]


class MapObject(d2game.location.MapObject):
    empty = False

    def __init__(self):
        self.watered = False
        d2game.location.MapObject.__init__(self, self.get_image())

    def get_pos(self):
        return int(self.rect.x / 32), int(self.rect.y / 32)

    def is_watered(self):
        return self.watered

    def get_image(self):
        return resources[self.type_id]


class Tree(MapObject):
    type_id = TREE_ID


class Rock(MapObject):
    type_id = ROCK_ID
    watered = False
    empty = True


class Town(MapObject):
    type_id = TOWN_ID
    points = ((1, 0), (-1, 0), (0, 1), (0, -1))
    empty = True

    def __init__(self):
        self.images = resources[self.type_id]
        MapObject.__init__(self)

    def get_image(self):
        if self.watered:
            return self.images[1]
        else:
            return self.images[0]

    def update_watered(self, level):
        x, y = self.get_pos()
        l = [level.locations[x + px][y + py] for px, py in self.points]
        w = [i for i in l if i.is_watered()]
        return len(w) > 0        
    
    def set_watered(self, watered):
        self.watered = watered
        self.image = self.get_image()
        

class Well(MapObject):
    type_id = WELL_ID
    watered = True
    empty = True


class Aqueduct(MapObject):
    type_id = AQUEDUCT_ID

    def __init__(self, images, points):
        self.images = images
        self.watered = False
        MapObject.__init__(self)
        self.points = points

    def get_image(self):
        if self.watered:
            return self.images[1]
        else:
            return self.images[0]

    def update_watered(self, level):
        x, y = self.get_pos()
        l = [level.locations[x + px][y + py] for px, py in self.points]
        w = [i for i in l if i.is_watered()]

        import logging
        logging.debug("Seek for watered points")
        logging.debug(self.points)
        logging.debug("Points are %s", str(l))
        logging.debug("I am at %s", str(self.get_pos()))
        logging.debug("Points are at %s", str([i.get_pos() for i in l]))
        logging.debug("Watered points are %s", str(w))
        logging.debug("%d watered points found", len(w))
        return len(w) > 0
    
    def set_watered(self, watered):
        self.watered = watered
        self.image = self.get_image()