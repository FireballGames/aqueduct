#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame.sprite


class Tile(pygame.sprite.Sprite):
    start_point = (0, 0)
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()


class MapObject(Tile):
    type_id = 0
    _layer = 10


class Location(Tile):
    def __init__(self, image):
        Tile.__init__(self, image)

        self.map_object = None

    def set_object(self, map_object):
        if self.map_object:
            self.map_object.kill()
        if map_object:
            self.map_object = map_object
            self.map_object.rect = self.rect
            self.map_object.rect.x = self.map_object.rect.x + (self.map_object.start_point[0] * 32)
            self.map_object.rect.y = self.map_object.rect.y + (self.map_object.start_point[1] * 32)
        else:
            self.map_object = None
        return self.map_object


class Terrain(Location):
    type_id = 0
    _layer = 1

    def __init__(self, image):
        Location.__init__(self, image)
