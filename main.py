#!/usr/bin/env python

import logging.config
import sys
import time

import schedule

import config
from presentation.max7219.max7219_scroller import Max7219Scroller

DEFAULT_ENCODING = "utf-8"
INFO_REFRESH_SECONDS = 5

logger = logging.getLogger()
current_provider = 0
providers = []
scroller = None


def _main():
    try:
        _configure_encoding()
        _configure_logging()
        _create_scroller()
        _run_scheduler()
    except KeyboardInterrupt:
        pass


def _configure_encoding():
    reload(sys)
    sys.setdefaultencoding(DEFAULT_ENCODING)


def _configure_logging():
    try:
        logging.config.fileConfig(config.LOGGING_CONFIG)
    except AttributeError:
        pass


def _create_scroller():
    scroller = Max7219Scroller()


def _run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    _main()
