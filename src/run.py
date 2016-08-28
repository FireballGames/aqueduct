#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():

    import os
    import config

    # config.RES_DIR = "{}/../res".format(os.path.dirname(os.path.abspath(__file__)))
    config.ROOT_DIR = "{}/..".format(os.path.dirname(os.path.abspath(__file__)))
    config.load()

    import logging
    logging.info('Starting')

    import config.resource
    import game.game
    import game.gui

    gui = game.gui.GUI()
    g = game.game.Game()
    gui.set_game(g)
    gui.set_background(config.resource.BACKGROUND)
    gui.draw_background()
    g.run()

    while g.is_running():
        gui.process_events()
        g.turn()
        gui.draw()
    g.quit()

if __name__ == "__main__":
    main()
