#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


ROOT_DIR = "{}/../..".format(os.path.dirname(__file__))
CONFIG_FILE = "{}/config/config.yml".format(ROOT_DIR)

config = dict()


def get_loglevel(loglevel):
    import logging

    level = getattr(logging, loglevel.upper())
    if not isinstance(level, int):
        return logging.WARNING
    return level


def load():
    global config, RES_DIR
    import logging
    import yaml

    with open(CONFIG_FILE, 'r') as f:
        config = yaml.load(f)
        RES_DIR = "{}/{}".format(ROOT_DIR, config.get("resource", "res"))

        log = config.get("logging", dict())
        log["level"] = get_loglevel(log.get("level"))
        logging.basicConfig(**log)

    logging.debug("Config data:{}".format(config))
    logging.debug("Resource dir is '{}'".format(RES_DIR))
