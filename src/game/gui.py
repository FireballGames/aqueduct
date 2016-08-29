#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import game
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
        d2gui.GUI.__init__(self, config.config["window"])

        import pygame
        self.show_logo()
        self.tool_panel = pygame.Surface((100, 100))

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

    def draw_cash(self):
        import pygame
        import pygame.font

        font = pygame.font.SysFont("monospace", 15)
        label = font.render(str(self.game.cash), True, (0, 185, 0))

        self.tool_panel.fill(pygame.Color(196, 196, 196))
        self.tool_panel.blit(label, (0, 0))

        screen = pygame.display.get_surface()
        screen.blit(self.tool_panel, (800, 600))

    def draw(self):
        import d2game
        if self.game.state == d2game.STATE_RUNNING:
            self.draw_cash()
        d2gui.GUI.draw(self)

    def process_event(self, event):
        d2gui.GUI.process_event(self, event)
        if event.type == game.AUTOCASH_EVENT:
            self.game.cash += 1

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
