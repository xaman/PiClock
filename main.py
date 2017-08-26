#!/usr/bin/env python

import schedule
import config
import logging.config

from formatter.crypto_formatter import CryptoFormatter
from model.crypto_id import CryptoId
from provider.crypto_provider import CryptoProvider

INFO_REFRESH_SECONDS = 5

logger = logging.getLogger()
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
    providers.append(CryptoProvider(CryptoId.ETHEREUM))
    providers.append(CryptoProvider(CryptoId.BITCOIN))
    for provider in providers:
        provider.initialize()


def _initialize_scheduler():
    schedule.every(INFO_REFRESH_SECONDS).seconds.do(_show_information)
    while True:
        schedule.run_pending()


def _show_information():
    for provider in providers:
        logger.info(CryptoFormatter().format(provider.get_value()))


if __name__ == '__main__':
    _main()
