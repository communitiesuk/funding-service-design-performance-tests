from common.common_methods import check_expected_status
from common.config import ROUND_STORE
from locust import HttpUser
from locust import task


class RoundStore(HttpUser):
    host = ROUND_STORE
    fund_id = "funding-service-design"
    round_id = "spring"

    @task
    def get_funding_round(self):
        """
        Performance test for GET /funds/{fund_id}/rounds/{round_id}
         that expects a 200
        """
        with self.client.get(
            f"/funds/{self.fund_id}/rounds/{self.round_id}", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_fund(self):
        """
        Performance test for GET /funds/{fund_id}/rounds that expects a 200
        """
        with self.client.get(
            f"/funds/{self.fund_id}/rounds", catch_response=True
        ) as response:
            check_expected_status(response, 200)
