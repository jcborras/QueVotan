#!/usr/bin/env python
# -*- coding: utf-8; mode: python; -*-

""" Common funcs and vars """
from datetime import datetime
from io import BytesIO
from os import getpid
from zipfile import is_zipfile, ZipFile

from requests import get, head

from logging import INFO, Formatter, StreamHandler, getLogger


def get_logger(name=__file__):
    handler = StreamHandler()
    fmt = "%(asctime)s:%(filename)16s:%(lineno)3d:%(levelname)s: %(message)s"
    handler.setFormatter(Formatter(fmt))
    handler.setLevel(INFO)
    logger = getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(INFO)
    return logger


logger = get_logger()


def fetch_zip(url, dstdir):
    logger.info('[PID={pid:n}] Fetching {s:s}'.format(pid=getpid(), s=url))
    t0 = datetime.now()
    x = get(url)
    d = datetime.now() - t0
    logger.info('\t[PID={pid:n}] GET completed after {d:.2f} s.'.format(
        pid=getpid(), d=d.total_seconds()))
    logger.info('\t[PID={pid:n}] Content-Type is {b:s}'.format(
        pid=getpid(), b=x.headers['Content-Type']))
    try:
        assert(x.headers['Content-Type'] == 'application/zip')
    except AssertionError:
        logger.fatal('[PID={pid:n}] Resource content mismatch: {s:s}\n'.format(
            pid=getpid(), s=url))
        return
    xx = BytesIO(x.content)
    logger.info('\t[PID={pid:n}] Expected content is {b:b}'.format(
        pid=getpid(), b=is_zipfile(xx)))
    assert(is_zipfile(xx))
    filename = dstdir + url.split('/')[-1]
    logger.info('\t[PID={pid:n}] Saving to {s:s}'.format(
        pid=getpid(), s=filename))
    with open(filename, 'wb') as f:
        f.write(x.content)
