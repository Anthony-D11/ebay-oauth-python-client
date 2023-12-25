# -*- coding: utf-8 -*-

'''
Authored by: Anthony Nguyen
'''

import platform
import logging

__version__ = '1.0.0'
Version = __version__  # for backward compatibility

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):

        def emit(self, record):
            pass

UserAgent = 'eBayOauthClient/%s Python/%s %s/%s' % (
    __version__,
    platform.python_version(),
    platform.system(),
    platform.release()
)

log = logging.getLogger('eBayOauthClient')

if not log.handlers:
    log.addHandler(NullHandler())


def get_version():
    return __version__


def set_stream_logger(level=logging.DEBUG, format_string=None):
    log.handlers = []

    if not format_string:
        format_string = "%(asctime)s %(name)s [%(levelname)s]:%(message)s"

    log.setLevel(level)
    fh = logging.StreamHandler()
    fh.setLevel(level)
    formatter = logging.Formatter(format_string)
    fh.setFormatter(formatter)
    log.addHandler(fh)