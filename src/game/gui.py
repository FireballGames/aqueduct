#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2gui
# import pygame


# DIR_KEYS = {
#     pygame.K_LEFT: "left",
#     pygame.K_RIGHT: "right",
#     pygame.K_UP: "up",
#     pygame.K_DOWN: "down",
# }


class GUI(d2gui.GUI):
    def mouse_event(self, mouse_pos):
        import logging
        logging.debug(mouse_pos)

        import d2game.location
        clicked = [s for s in self.game.level.entities if s.rect.collidepoint(mouse_pos)]
        for c in clicked:
            if isinstance(c, d2game.location.Location):
                c.set_object(self.game.level.aqueducts[0])
                self.game.level.entities.add(c.map_object)
        logging.debug(clicked)
