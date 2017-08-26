#!/usr/bin/env python

import schedule
import config
import logging
from provider.crypto_provider import CryptoProvider

INFO_REFRESH_SECONDS = 5

logger = logging.getLogger("root")
current_provider = 0
providers = []


def _main():
    _configure_logging()
    _create_providers()
    _initialize_scheduler()


def _configure_logging():
    try:
        logging.config.fileConfig(config.LOGGING_CONFIG)
    except AttributeError:
        pass


def _create_providers():
    providers.append(CryptoProvider("bitcoin", "EUR"))
    providers.append(CryptoProvider("ethereum", "EUR"))
    for provider in providers:
        provider.initialize()


def _initialize_scheduler():
    schedule.every(INFO_REFRESH_SECONDS).seconds.do(_show_information)
    while True:
        schedule.run_pending()


def _show_information():
    print "Show information"


if __name__ == '__main__':
    _main()
