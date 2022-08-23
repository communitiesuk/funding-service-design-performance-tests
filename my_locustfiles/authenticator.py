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
            "/service/magic-links/landing/TUwinPwR", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # Tests using Swagger API as a reference
    @task
    def post_create_new_magic_link(self):
        """
        Performance test for POST create new magic link that expects a 201
        """
        with self.client.post("/magic-links", json={"email":"a@example.com", "redirectUrl":"https://example.com/redirect-url"}, catch_response=True
        ) as response:
            check_expected_status(response, 201)

    @task
    def get_search_magic_link(self):
        """
        Performance test for GET search magic link that expects a 200
        """
        with self.client.get("/magic-links", catch_response=True
        ) as response:
            check_expected_status(response, 200)