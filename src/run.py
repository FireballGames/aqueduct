#!/usr/bin/env python
# -*- coding: utf-8 -*-


import config


def main():
    import os

    # config.RES_DIR = "{}/../res".format(os.path.dirname(os.path.abspath(__file__)))
    config.ROOT_DIR = "{}/..".format(os.path.dirname(os.path.abspath(__file__)))
    config.load()

    import game
    import game.gui

    gui = game.gui.GUI()
    g = game.Game()
    gui.set_game(g)
    g.run()

    while g.is_running():
        gui.process_events()
        g.turn()
        gui.draw()
    g.quit()

if __name__ == "__main__":
    main()
