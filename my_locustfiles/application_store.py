from locust import HttpUser, task
from common.config import Configs
import json
from common.common_methods import Common


class ApplicationStore(HttpUser):

    host = Configs.config["Hosts"]["ApplicationStore"]
    new_application_json_file = open(
        "./data/application_store/new_application.json", "r"
    )
    new_application_json = json.loads(new_application_json_file.read())
    fund_name = "slugified_test_fund_name"

    @task
    def get_all_funds(self):
        with self.client.get("/fund/all_funds", catch_response=True) as response:
            Common.check_expected_status(response, 200)

    @task
    def post_new_application(self):
        with self.client.post(
            "/fund/new_application",
            json=self.new_application_json,
            catch_response=True,
        ) as response:
            Common.check_expected_status(response, 201)

    @task
    def get_fund(self):
        with self.client.get(
            f"/fund/{self.fund_name}", catch_response=True
        ) as response:
            Common.check_expected_status(response, 200)
