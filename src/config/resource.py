#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config


BACKGROUND = "{}/back.png".format(config.RES_DIR)
PLAYER = "{}/well.png".format(config.RES_DIR)

Tiles = [
    "{}/tiles/grass.png".format(config.RES_DIR),
    "{}/tiles/water.png".format(config.RES_DIR),
    "{}/tiles/tree.png".format(config.RES_DIR),
    "{}/tiles/rock.png".format(config.RES_DIR),
]
Towns = [
    "{}/images/house.png".format(config.RES_DIR),
]
Wells = [
    "{}/images/tank_full.png".format(config.RES_DIR),
    "{}/images/tank_empty.png".format(config.RES_DIR),
]

HERO_SIZE = (91, 173)
