import json

from common.common_methods import check_expected_status
from common.config import AUTHENTICATOR
from locust import HttpUser
from locust import task

class Authenticator(HttpUser):

    host = AUTHENTICATOR
    fund_id = "47aef2f5-3fcb-4d45-acb5-f0152b5f03c4"
    round_id = "c603d114-5364-4474-a0c4-c41cbf4d3bbd"

    @task
    def get_magic_link(self):
        """
        Performance test for GET magic links that expects a 200
        """
        with self.client.get(
            "/service/magic-links/new?/{self.fund_id}/{self.round_id}", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_magic_link_email(self):
        """
        Performance test for GET magic link email that expects a 200
        """
        with self.client.get(
            "/service/magic-links/check-email?email=test%40test.com", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_magic_link_email_id(self):
        """
        Performance test for GET magic link email ID that expects a 200
        """
        with self.client.get(
            "/service/magic-links/landing/TUwinPwR"
        ) as response:
            check_expected_status(response, 200)