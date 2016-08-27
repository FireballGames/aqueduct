#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game
import game.player
import game.levelmap

import pygame

TITLE = "Aqueduct"
BACKGROUND_COLOR = pygame.Color(255, 255, 0)


class Game(d2game.Game):
    def new_hero(self):
        return game.player.Player()

    def next_level(self):
        self.level = game.levelmap.LevelMap(self.hero)
        self.level.generate_map()

        import logging
        self.level.generate_surface()
        return self.level

    def turn(self):
        d2game.Game.turn(self)
        for e in self.level.enemies:
            e.move(self.level)
