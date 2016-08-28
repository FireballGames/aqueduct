#!/usr/bin/env python
# -*- coding: utf-8 -*-


import d2game
import game
import game.player
import game.levelmap


class Game(d2game.Game):
    def new_hero(self):
        return None

    def next_level(self):
        self.level = game.levelmap.LevelMap(self.hero)
        self.level.generate_map()
        self.level.generate_surface()
        self.cash = 10

        import pygame.time
        pygame.time.set_timer(game.AUTOCASH_EVENT, game.AUTOCASH_TIME)
        return self.level

    def turn(self):
        d2game.Game.turn(self)
        for e in self.level.enemies:
            e.move(self.level)
