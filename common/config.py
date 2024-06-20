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
    "https://funding-service-design-application-store-dev.london.cloudapps.digital",  
)

ASSESSMENT_STORE = getenv (
    "TARGET_URL_ASSESSMENT_STORE",
    "https://funding-service-design-assessment-store-dev.london.cloudapps.digital",
)


FUND_ID  = "47aef2f5-3fcb-4d45-acb5-f0152b5f03c4"
ROUND_ID = "6af19a5e-9cae-4f00-9194-cf10d2d7c8a7"
USER_AGENT = "locust performance tests"


print("======= URLs ==========")
print(f"FUND_STORE: {FUND_STORE}")
print(f"APPLICATION_STORE: {APPLICATION_STORE}")
print(f"ASSESSMENT_STORE:  {ASSESSMENT_STORE}")
