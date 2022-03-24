from locust import HttpUser, task
from common.config import Configs
from common.common_methods import Common


class FundStore(HttpUser):
    host = Configs.config["Hosts"]["FundStore"]
    fund_name = "harry-s-breakfast-fund"

    @task
    def list_all_funds(self):
        with self.client.get("/funds", catch_response=True) as response:
            Common.check_expected_status(response, 200)

    @task
    def post_new_application(self):
        with self.client.post(
            f"/funds/search/?search_items={self.fund_name}", catch_response=True
        ) as response:
            Common.check_expected_status(response, 200)

    @task
    def get_fund(self):
        with self.client.get(
            f"/funds/{self.fund_name}", catch_response=True
        ) as response:
            Common.check_expected_status(response, 200)
