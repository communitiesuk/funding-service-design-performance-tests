from common.common_methods import check_expected_status
from common.config import FUND_STORE
from common.config import FUND_ID
from common.config import ROUND_ID
from common.config import USER_AGENT
from locust import HttpUser
from locust import task


class FundStore(HttpUser):
    host = FUND_STORE
    fund_id = FUND_ID
    round_id = ROUND_ID
    search_query = "breakfast,fund"

    @task
    def get_list_of_all_funds(self):
        """
        Performance test for GET /funds/ that expects a 200
        """
        with self.client.get("/funds", 
        catch_response=True,
        headers={"User-Agent": USER_AGENT},
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_a_fund(self):
        """
        Performance test for GET /funds/{fund_id} that expects a 200
        """
        with self.client.get(
            f"/funds/{self.fund_id}", 
            headers={"User-Agent": USER_AGENT},
            catch_response=True,
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_all_rounds_for_a_fund(self):
        """
        Performance test for GET /funds/{fund_id}/rounds that expects a 200
        """
        with self.client.get(
            f"/funds/{self.fund_id}/rounds",
            headers={"User-Agent": USER_AGENT},
            catch_response=True,
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_data_on_specific_round_for_specific_fund(self):
        """
        Performance test for GET /funds/{fund_id}/rounds/{round_id}
         that expects a 200
        """
        with self.client.get(
            f"/funds/{self.fund_id}/rounds/{self.round_id}", 
            headers={"User-Agent": USER_AGENT},
            catch_response=True,
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_list_of_flag_allocations(self):
        """
        Performance test for GET /funds/{fund_id}/rounds/{round_id}/available_flag_allocations
         that expects a 200
        """
        with self.client.get(
            f"/funds/{self.fund_id}/rounds/{self.round_id}/available_flag_allocations", 
            headers={"User-Agent": USER_AGENT},
            catch_response=True,
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_application_sections_for_given_round(self):
        """
        Performance test for GET /funds/{fund_id}/rounds/{round_id}/sections/application
         that expects a 200
        """
        with self.client.get(
            f"/funds/{self.fund_id}/rounds/{self.round_id}/sections/application", 
            headers={"User-Agent": USER_AGENT},
            catch_response=True,
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_search_a_fund(self):
        """
        Performance test for GET /funds?search_items={search_query}
         that expects a 200.
        """
        with self.client.get(
            f"/funds?search_items={self.search_query}",
            headers={"User-Agent": USER_AGENT},
            catch_response=True,
        ) as response:
            check_expected_status(response, 200)  