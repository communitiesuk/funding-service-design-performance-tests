import json

from common.common_methods import check_expected_status
from common.config import APPLICATION_STORE
from common.config import USER_AGENT
from locust import HttpUser
from locust import task


class ApplicationStore(HttpUser):

    host = APPLICATION_STORE
    new_application_json_file = open(
        "./data/application_store/new_application.json", "r"
    )
    new_application_json = json.loads(new_application_json_file.read())

    @task
    def post_new_application(self):
        """
        Performance test for POST /applications that expects a 201
        """
        with self.client.post(
            "/applications",
            json=self.new_application_json,
            headers={"User-Agent": USER_AGENT},
            catch_response=True, 
        ) as response:
             check_expected_status(response, 201)
           
    @task
    def get_applications_for_a_fund(self):
        """
        Performance test for GET /applications?fund_id={fund_id} that expects a 200
        """
        with self.client.get(
            "/applications?fund_id=''",
            headers={"User-Agent": USER_AGENT},
            catch_response=True,
        ) as response:
             check_expected_status(response, 200)
    
    @task
    def get_report_on_started_and_submitted_applications_for_a_fund(self):
        """
        Performance test for GET /applications/reporting/applications_statuses_data that expects a 200
        """
        with self.client.get(
            "/applications/reporting/applications_statuses_data",
            headers={"User-Agent": USER_AGENT},
            catch_response=True,
        ) as response:
             check_expected_status(response, 200)

