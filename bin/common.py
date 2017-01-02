#!/usr/bin/env python
# -*- coding: utf-8; mode: python; -*-

""" Common funcs and vars """

from logging import INFO, Formatter, StreamHandler, getLogger

CONGRESO = ['02201606_MESA.zip', '02201512_MESA.zip', '02201111_MESA.zip',
            '02200803_MESA.zip', '02200403_MESA.zip', ]

SENADO = ['03201606_MESA.zip', '03201512_MESA.zip', '03201111_MESA.zip',
          '03200803_MESA.zip', '03200403_MESA.zip', ]


def get_logger(name):
    handler = StreamHandler()
    fmt = "%(asctime)s:%(filename)16s:%(lineno)3d:%(levelname)s: %(message)s"
    handler.setFormatter(Formatter(fmt))
    handler.setLevel(INFO)
    logger = getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(INFO)
    return logger
