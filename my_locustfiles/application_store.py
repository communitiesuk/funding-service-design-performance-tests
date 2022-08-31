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
    status_only = "IN_PROGRESS"


    @task
    def put_new_application(self):
        """
        Performance test for PUT /applications/sections that expects a 201
        """
        with self.client.put(
            "/applications/forms",
            json=self.new_application_json,
            catch_response=True,
        ) as response:
            check_expected_status(response, 201)

    @task
    def get_applications_for_a_fund(self):
        """
        Performance test for GET /applications?fund_id={fund_id} that expects a 200
        """
        with self.client.get(
            "/applications?fund_id=''", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_applications_status(self):
        """
        Performance test for GET /applications?status_only={status_only} that expects a 200
        """
        with self.client.get(
            "/applications?status_only='/{self.status_only}'", catch_response=True
        ) as response:
            check_expected_status(response, 200)
