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
        TOWN_ID: config.resource.load(config.resource.Towns, 0),
        WELL_ID: config.resource.load(config.resource.Wells, 0),
        AQUEDUCT_ID: [
            config.resource.load(config.resource.Aqueducts, 0),
            config.resource.load(config.resource.Aqueducts, 1),
        ],
    }
    return resources


def load_aqueduct(id, points, rotation):
    import pygame.transform
    image = resources[AQUEDUCT_ID][id]
    image = pygame.transform.rotate(image, rotation)
    return image, points


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
    def __init__(self):
        d2game.location.MapObject.__init__(self, self.get_image())

        self.watered = False

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


class Town(MapObject):
    type_id = TOWN_ID


class Well(MapObject):
    type_id = WELL_ID
    watered = True


class Aqueduct(MapObject):
    type_id = AQUEDUCT_ID

    def __init__(self, image, points):
        self.image = image
        MapObject.__init__(self)
        self.points = points

    def get_image(self):
        return self.image

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
