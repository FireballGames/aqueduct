#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import game
import d2gui

import pygame
import pygame.image
import pygame.font
import pygame.draw


class Tools(pygame.Surface):
    def __init__(self):
        pygame.Surface.__init__(self, (100, 100))
        self.font = pygame.font.SysFont("monospace", 15)
        self.aqueducts = [None for i in range(0, 6)]
        self.selected_id = 0

    def draw_aqueduct(self, level):
        self.aqueducts = [level.get_random_aqueduct() for i in range(0, 6)]

    def tool_pos(self, id):
        return (id % 3) * 32, int(id / 3) * 32 + 32

    def update_cash(self, cash):
        label = self.font.render(str(cash), True, (0, 185, 0))

        self.fill(pygame.Color(196, 196, 196))
        self.blit(label, (32, 0))

        for i, a in enumerate(self.aqueducts):
            self.blit(a.image, self.tool_pos(i))
        pygame.draw.rect(self, pygame.Color(0, 185, 0), pygame.Rect(self.tool_pos(self.selected_id), (32, 32)), 1)

    def draw_tools(self):
        screen = pygame.display.get_surface()
        screen.blit(self, (800, 600))
        
    def active_tool(self):
        return self.aqueducts[self.selected_id]


class GUI(d2gui.GUI):
    def __init__(self):
        d2gui.GUI.__init__(self, config.config["window"])

        self.show_logo()

        self.tool_panel = Tools()

    def show_logo(self):
        import config.resource
        screen = pygame.display.get_surface()
        logo = pygame.image.load(config.resource.LOGO)
        screen.blit(logo, (0, 0))

    def run_game(self):
        import d2game
        if self.game.state == d2game.STATE_START:
            self.game.run()
            self.tool_panel.draw_aqueduct(self.game.level)
            return True
        return False

    def draw_cash(self):
        self.tool_panel.update_cash(self.game.cash)
        self.tool_panel.draw_tools()

    def draw(self):
        import d2game
        d2gui.GUI.draw(self)
        if self.game.state == d2game.STATE_RUNNING:
            self.draw_cash()

    def autocash(self):
        self.game.cash += self.game.level.wages()
        self.game.turn()
        # self.draw_background()
        # self.update()
      
    def process_event(self, event):
        d2gui.GUI.process_event(self, event)
        if event.type == game.AUTOCASH_EVENT:
            self.autocash()

    def key_event(self, key, down):
        if self.run_game():
            return 0

        d2gui.GUI.key_event(self, key, down)

    def mouse_event(self, mouse_pos):
        if self.run_game():
            return 0

        import logging
        logging.debug("Mouse is at %s", str(mouse_pos))

        import d2game.location
        clicked = [s for s in self.game.level.entities if s.rect.collidepoint(mouse_pos)]
        for c in clicked:
            if isinstance(c, d2game.location.Location):
                if self.game.can_build(c):
                    self.game.cash -= 10
                    a = self.game.level.set_aqueduct(c, self.tool_panel.active_tool())
                    self.tool_panel.draw_aqueduct(self.game.level)
        logging.debug(clicked)
