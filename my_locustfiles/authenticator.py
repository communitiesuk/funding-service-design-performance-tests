import json

from common.common_methods import check_expected_status
from common.config import AUTHENTICATOR
from locust import HttpUser
from locust import task

class Authenticator(HttpUser):

    host = AUTHENTICATOR
    fund_id = "47aef2f5-3fcb-4d45-acb5-f0152b5f03c4"
    round_id = "c603d114-5364-4474-a0c4-c41cbf4d3bbd"

    # Click Start now
    @task(5)
    def get_click_start(self):
        """
        Performance test for GET click start that expects a 200
        """
        with self.client.get(
            "/service/magic-links/new?/{self.fund_id}/{self.round_id}", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # Enter email
    @task(5)
    def get_magic_link_email(self):
        """
        Performance test for GET magic link email that expects a 200
        """
        with self.client.get(
            "/service/magic-links/check-email?email=test%40test.com", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # Click magic link
    @task(5)
    def get_magic_link_id(self):
        """
        Performance test for GET magic link ID that expects a 200
        """
        with self.client.get(
            "/service/magic-links/landing/jQsEppja", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # Test below using Swagger API as a reference
    @task(1)
    def post_create_new_magic_link(self):
        """
        Performance test for POST create new magic link that expects a 201
        """
        with self.client.post("/magic-links", json={"email":"a@example.com", "redirectUrl":"https://example.com/redirect-url"}, catch_response=True
        ) as response:
            check_expected_status(response, 201)