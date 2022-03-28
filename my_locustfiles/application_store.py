import json

from common.common_methods import check_expected_status
from common.config import APPLICATION_STORE
from locust import HttpUser
from locust import task


class ApplicationStore(HttpUser):

    host = APPLICATION_STORE
    new_application_json_file = open(
        "./data/application_store/new_application.json", "r"
    )
    new_application_json = json.loads(new_application_json_file.read())
    fund_name = "slugified_test_fund_name"

    @task
    def get_all_funds(self):
        """
        Performance test for GET /fund/all_funds that expects a 200
        """
        with self.client.get(
            "/fund/all_funds", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    @task
    def post_new_application(self):
        """
        Performance test for POST /fund/new_application that expects a 201
        """
        with self.client.post(
            "/fund/new_application",
            json=self.new_application_json,
            catch_response=True,
        ) as response:
            check_expected_status(response, 201)

    @task
    def get_fund(self):
        """
        Performance test for GET /fund/{fund_name} that expects a 200
        """
        with self.client.get(
            f"/fund/{self.fund_name}", catch_response=True
        ) as response:
            check_expected_status(response, 200)
