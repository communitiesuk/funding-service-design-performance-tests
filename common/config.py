"""
Application Config
"""
from os import getenv


FUND_STORE = getenv(
    "TARGET_URL_FUND_STORE",
    "https://funding-service-design-fund-store-dev.london.cloudapps.digital",
)
APPLICATION_STORE = getenv(
    "TARGET_URL_APPLICATION_STORE",
    "https://funding-service-design-application-store-dev.london.cloudapps.digital",  # noqa
)
