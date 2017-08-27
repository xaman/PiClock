#!/usr/bin/env python

import logging.config

import schedule
import time

import config
from presentation.scroller import Scroller

INFO_REFRESH_SECONDS = 5

logger = logging.getLogger()
current_provider = 0
providers = []
scroller = None


def _main():
    try:
        _configure_logging()
        _initialize_scroller()
        _run_scheduler()
    except KeyboardInterrupt:
        pass


def _configure_logging():
    try:
        logging.config.fileConfig(config.LOGGING_CONFIG)
    except AttributeError:
        pass


def _initialize_scroller():
    scroller = Scroller()
    scroller.initialize()


def _run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    _main()
