#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame.sprite
import pygame.image


class SpriteLib(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.type_id = id
        self.start_point = (0, 0)
