from common.common_methods import check_expected_status
from common.config import FUND_STORE
from locust import HttpUser
from locust import task


class FundStore(HttpUser):
    host = FUND_STORE
    fund_name = "harry-s-breakfast-fund"

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
        Performance test for GET /funds?search_items={fund_name}
         that expects a 200.
        """
        with self.client.get(
            f"/funds?search_items={self.fund_name}",
            catch_response=True,
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_fund(self):
        """
        Performance test for GET /funds/{fund_name} that expects a 200
        """
        with self.client.get(
            f"/funds/{self.fund_name}", catch_response=True
        ) as response:
            check_expected_status(response, 200)
