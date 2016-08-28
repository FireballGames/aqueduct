#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config


LOGO = "{}/title.png".format(config.RES_DIR)
PLAYER = "{}/well.png".format(config.RES_DIR)

Tiles = [
    "{}/tiles/grass.png".format(config.RES_DIR),
    "{}/tiles/water.png".format(config.RES_DIR),
    "{}/tiles/tree.png".format(config.RES_DIR),
    "{}/tiles/rock.png".format(config.RES_DIR),
]
Towns = [
    "{}/images/house_without_water.png".format(config.RES_DIR),
]
Wells = [
    "{}/images/tank_full.png".format(config.RES_DIR),
    "{}/images/tank_empty.png".format(config.RES_DIR),
]
Aqueducts = [
    # "{}/images/aqueduct_full.png".format(config.RES_DIR),
    "{}/images/aqueduct_empty.png".format(config.RES_DIR),
    # "{}/images/aqueduct_corner_full.png".format(config.RES_DIR),
    "{}/images/aqueduct_corner_empty.png".format(config.RES_DIR),
]

HERO_SIZE = (91, 173)
