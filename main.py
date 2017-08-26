#!/usr/bin/env python
import time
import schedule
import config
import logging
from provider.crypto_provider import CryptoProvider

providers = []


def _main():
    _configure_logging()
    _create_providers()
    while True:
        schedule.run_pending()
        time.sleep(1)


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


if __name__ == '__main__':
    _main()
