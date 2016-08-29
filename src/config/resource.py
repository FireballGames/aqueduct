#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config


LOGO = "{}/title.png".format(config.RES_DIR)
# PLAYER = "{}/well.png".format(config.RES_DIR)
# HERO_SIZE = (91, 173)
TILE_SIZE = (32, 32)

Tiles = [
    "{}/tiles/grass.png".format(config.RES_DIR),
    "{}/tiles/water.png".format(config.RES_DIR),
    "{}/tiles/tree.png".format(config.RES_DIR),
    "{}/tiles/rock.png".format(config.RES_DIR),
]
Towns = [
    "{}/units/house_without_water.png".format(config.RES_DIR),
]
Wells = [
    "{}/units/tank_full.png".format(config.RES_DIR),
    "{}/units/tank_empty.png".format(config.RES_DIR),
]
Aqueducts = [
    "{}/aqueduct/aqueduct_empty.png".format(config.RES_DIR),
    "{}/aqueduct/aqueduct_corner_empty.png".format(config.RES_DIR),
]
