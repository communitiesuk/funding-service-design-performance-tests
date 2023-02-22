from common.common_methods import check_expected_status
from common.config import FUND_STORE
from common.config import FUND_ID
from common.config import ROUND_ID
from locust import HttpUser
from locust import task


class FundStore(HttpUser):
    host = FUND_STORE
    fund_id = FUND_ID
    round_id = ROUND_ID
    search_query = "breakfast,fund"

    @task
    def list_all_funds(self):
        """
        Performance test for GET /funds/ that expects a 200
        """
        with self.client.get("/funds", catch_response=True) as response:
            check_expected_status(response, 200)

    @task
    def get_a_fund_search(self):
        """
        Performance test for GET /funds?search_items={search_query}
         that expects a 200.
        """
        with self.client.get(
            f"/funds?search_items={self.search_query}",
            catch_response=True,
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_fund(self):
        """
        Performance test for GET /funds/{fund_id} that expects a 200
        """
        with self.client.get(
            f"/funds/{self.fund_id}", catch_response=True
        ) as response:
            check_expected_status(response, 200)

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