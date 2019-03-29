#!/usr/bin/env python
# -*- coding: utf-8; mode: python; -*-

from datetime import datetime
from io import BytesIO
from logging import getLevelName, getLogger
from os import getpid
from zipfile import is_zipfile, ZipFile

from requests import get, head


__author__ = 'Juan Carlos Borrás'
__version__ = '0.0.1'


_, *tail = __name__.split('.')
logger = getLogger(_)
logger.setLevel(getLevelName('CRITICAL'))


def content_type_fails(url):
    """Issues a HEAD request to check that the content type is
    application/zip
    """
    pid = getpid()
    logger.info('[PID={pid:n}] Fetching {s:s}'.format(pid=pid, s=url))
    t0 = datetime.now()
    x = head(url)
    d = datetime.now() - t0
    logger.info('\t[PID={pid:n}] HEAD completed after {d:.2f} s.'.format(
        pid=pid, d=d.total_seconds()))
    logger.info('\t[PID={pid:n}] Content-Type is {b:s}'.format(
        pid=pid, b=x.headers['Content-Type']))
    if not x.headers['Content-Type'] == 'application/zip':
        _ = '[PID={pid:n}] Content-type mismatch: {s:s}\n'
        logger.error(_.format(pid=pid, s=url))
        return True
    return False


def fetch_zip(url, dst_filename=None):
    """Fetches a zip file. It'll store it in dst_filename if some proper
    filename is specified"""
    pid = getpid()
    if content_type_fails(url):
        raise RuntimeError('Target is not of content type application/zip')
    logger.info('[PID={pid:n}] Fetching {s:s}'.format(pid=pid, s=url))
    t0 = datetime.now()
    x = get(url)
    d = datetime.now() - t0
    logger.info('\t[PID={pid:n}] GET completed after {d:.2f} s.'.format(
        pid=pid, d=d.total_seconds()))
    xx = BytesIO(x.content)
    logger.info('\t[PID={pid:n}] Expected content is {b:b}'.format(
        pid=pid, b=is_zipfile(xx)))
    assert(is_zipfile(xx))
    if dst_filename:
        logger.info('\t[PID={pid:n}] Saving to {s:s}'.format(
            pid=pid, s=dst_filename))
        with open(dst_filename, 'wb') as f:
            f.write(x.content)
    return xx
