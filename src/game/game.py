#!/usr/bin/env python
# -*- coding: utf-8 -*-


import d2game
import game
import game.levelmap


class Game(d2game.Game):
    level_id = 0
    def new_hero(self):
        return None

    def next_level(self):
        self.level_id += 1
        self.level = game.levelmap.LevelMap(self.hero)
        self.level.level_id = self.level_id
        self.level.generate_map()
        self.level.generate_surface()
        self.cash = 10

        import pygame.time
        pygame.time.set_timer(game.AUTOCASH_EVENT, game.AUTOCASH_TIME)
        return self.level

    def turn(self):
        d2game.Game.turn(self)
        if not self.level.update_watering():
            self.state = d2game.STATE_START

    def can_build(self, tile):
        if self.cash < 10:
            return False
        return tile.can_build()