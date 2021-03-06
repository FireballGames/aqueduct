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

    # import config.resource
    import d2game
    import game.game
    import game.gui

    gui = game.gui.GUI()
    g = game.game.Game()
    gui.set_game(g)

    while g.state == d2game.STATE_START:
        gui.process_events()
        gui.update()

    # gui.set_background(config.resource.BACKGROUND)
    g.run()
    gui.draw_background()

    while g.is_running():
        gui.process_events()
        # g.turn()
        gui.update()

    g.quit()

if __name__ == "__main__":
    main()
