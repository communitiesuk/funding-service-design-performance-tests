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

ASSESSMENT_STORE = getenv (
    "TARGET_URL_ASESSMENT_STORE",
    "https://funding-service-design-assessment-store-dev.london.cloudapps.digital/",
)

print("======= URLs ==========")
print(f"FUND_STORE: {FUND_STORE}")
print(f"APPLICATION_STORE: {APPLICATION_STORE}")
print(f"ASSESSMENT_STORE:  {ASSESSMENT_STORE}")
