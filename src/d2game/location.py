#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame.sprite


class Tile(pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)

        self.image = sprite.image
        self.rect = self.image.get_rect()


class Terrain(pygame.sprite.Sprite):
    pass


class ObjectType(Tile):
    def __init__(self, sprite):
        Tile.__init__(self, sprite)


class MapObject(Tile):
    type_id = 0
    _layer = 10

    def __init__(self, object_type):
        Tile.__init__(self, object_type)

        self.object_type = object_type


class Location(Tile):
    def __init__(self, terrain, **kargs):
        Tile.__init__(self, terrain)

        self._layer = 1
        self.terrain = terrain

        self.map_object = None

        object_type = kargs.get("object_type")
        if object_type:
            self.set_object(object_type)

    def set_object(self, map_object):
        if map_object:
            self.map_object = MapObject(map_object)
            self.map_object.rect = self.rect
        else:
            self.map_object = None
        return self.map_object
