#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml


ROOT_DIR = "{}/../..".format(os.path.dirname(__file__))
# RES_DIR = "{}/res".format(ROOT_DIR)
CONFIG_FILE = "{}/config/config.yml".format(ROOT_DIR)

BLOCK = 24
# WIN_WIDTH = 800   # 32 * BLOCK
# WIN_HEIGHT = 600  # 24 * BLOCK

config = dict()


def load():
    global config, RES_DIR

    with open(CONFIG_FILE, 'r') as f:
        config = yaml.load(f)
        WINDOW = config.get('window', dict())
        # WIN_WIDTH = WINDOW.get('width', WIN_WIDTH)
        # WIN_HEIGHT = WINDOW.get('height', WIN_HEIGHT)
        # DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
        RES_DIR = "{}/{}".format(ROOT_DIR, config.get("resource", "res"))

    print(config)
    print(RES_DIR)
