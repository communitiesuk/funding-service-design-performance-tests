import json

from common.common_methods import check_expected_status
from common.config import ACCOUNT
from locust import HttpUser
from locust import task

class Account(HttpUser):

    host = ACCOUNT
    email_address = "test@test.com"
   
    # Return account data
    @task(5)
    def get_account_data(self):
        """
        Performance test for GET account data that expects a 200
        """
        with self.client.get(
            f"/accounts?email_address={self.email_address}", catch_response=True
        ) as response:
            check_expected_status(response, 200)
    