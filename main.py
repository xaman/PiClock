#!/usr/bin/env python

import logging.config

import schedule

import config
from domain.crypto.coin_id import CoinId
from provider.crypto_provider import CryptoProvider
from provider.date_provider import DateProvider
from provider.weather_provider import WeatherProvider

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
    providers.append(DateProvider())
    providers.append(WeatherProvider("Madrid, ES"))
    providers.append(CryptoProvider(CoinId.ETHEREUM))
    providers.append(CryptoProvider(CoinId.BITCOIN))
    for provider in providers:
        provider.initialize()


def _initialize_scheduler():
    schedule.every(INFO_REFRESH_SECONDS).seconds.do(_show_information)
    while True:
        schedule.run_pending()


def _show_information():
    for provider in providers:
        logger.info(provider.get_formatted_value())


if __name__ == '__main__':
    _main()
