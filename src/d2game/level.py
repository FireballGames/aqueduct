#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame


class Level():
    def __init__(self, player):
        self.background = None
        self.entities = pygame.sprite.Group()
        self.entities.add(player)
        self.enemies = self.generate_enemies()
        for enemy in self.enemies:
            self.entities.add(enemy)

    def generate_enemies(self):
        return []
