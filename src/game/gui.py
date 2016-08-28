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
    def __init__(self):
        d2gui.GUI.__init__(self)
        self.show_logo()

    def show_logo(self):
        import config.resource
        import pygame
        import pygame.image
        screen = pygame.display.get_surface()
        logo = pygame.image.load(config.resource.LOGO)
        screen.blit(logo, (0, 0))

    def run_game(self):
        import d2game
        if self.game.state == d2game.STATE_START:
            self.game.run()
            return True
        return False

    def key_event(self, key, down):
        if self.run_game():
            return 0

        d2gui.GUI.key_event(self, key, down)

    def mouse_event(self, mouse_pos):
        if self.run_game():
            return 0

        import logging
        logging.debug(mouse_pos)

        import d2game.location
        clicked = [s for s in self.game.level.entities if s.rect.collidepoint(mouse_pos)]
        for c in clicked:
            if isinstance(c, d2game.location.Location):
                a = self.game.level.set_random_aqueduct(c)
        logging.debug(clicked)
