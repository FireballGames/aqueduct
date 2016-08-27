#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import config.resource
import d2game.player

# import game.entity

START_POS = (16 * config.BLOCK, 15 * config.BLOCK)


class Player(d2game.player.Player):  # (game.entity.Entity):
    def __init__(self):
        d2game.player.Player.__init__(self)

        import pygame.image
        import pygame.rect

        self.image = pygame.image.load(config.resource.PLAYER)
        self.rect = pygame.Rect(100, 100, 50, 50)
