#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2gui
import pygame


DIR_KEYS = {
    pygame.K_LEFT: "left",
    pygame.K_RIGHT: "right",
    pygame.K_UP: "up",
    pygame.K_DOWN: "down",
}


class GUI(d2gui.GUI):
    def key_event(self, key, down):
        d2gui.GUI.key_event(self, key, down)
        direction = DIR_KEYS.get(key)
        if direction:
            self.player.go(direction, down)
