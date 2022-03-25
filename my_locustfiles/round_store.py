from locust import HttpUser, task
from common.config import ROUND_STORE
from common.common_methods import check_expected_status


class RoundStore(HttpUser):
    host = ROUND_STORE
    fund_id = "funding-service-design"
    round_id = "spring"

    @task
    def get_funding_round(self):
        """
        Performance test for GET /fund/{fund_id}/round/{round_id} that expects a 200
        """
        with self.client.get(
            f"/fund/{self.fund_id}/round/{self.round_id}", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_fund(self):
        """
        Performance test for GET /fund/{fund_id} that expects a 200
        """
        with self.client.get(
            f"/fund/{self.fund_id}", catch_response=True
        ) as response:
            check_expected_status(response, 200)
