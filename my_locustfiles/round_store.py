from locust import HttpUser, task
from common.config import Configs
from common.common_methods import Common


class RoundStore(HttpUser):
    host = Configs.config["Hosts"]["RoundStore"]
    fund_id = "funding-service-design"
    round_id = "spring"

    @task
    def get_funding_round(self):
        with self.client.get(
            f"/fund/{self.fund_id}/round/{self.round_id}", catch_response=True
        ) as response:
            Common.check_expected_status(response, 200)

    @task
    def get_fund(self):
        with self.client.get(f"/fund/{self.fund_id}", catch_response=True) as response:
            Common.check_expected_status(response, 200)
