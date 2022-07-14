import json

from common.common_methods import check_expected_status
from common.config import ASSESSMENT_STORE
from locust import HttpUser
from locust import task