#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.level


class LevelMap(d2game.level.Level):
    def __init__(self, player):
        d2game.level.Level.__init__(self, player)
        self.xsize = 16
        self.ysize = 16

    def generate_map(self):
        self.locations = [[0] * self.ysize for i in range(self.xsize)]

    def generate_surface(self):
        pass
