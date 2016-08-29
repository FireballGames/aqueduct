#!/usr/bin/env python
# -*- coding: utf-8 -*-


from cx_Freeze import setup, Executable

setup(
    name = "aqueduct",
    version = "0.1",
    description = "Ludum Dare",
    executables = [Executable("src/run.py")]
)