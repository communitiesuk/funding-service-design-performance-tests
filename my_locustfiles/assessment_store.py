import json

from common.common_methods import check_expected_status
from common.config import ASSESSMENT_STORE
from locust import HttpUser
from locust import task

class AssessmentStore(HttpUser):
    host = ASSESSMENT_STORE
    assessment_id = 1
    fund_id = "47aef2f5-3fcb-4d45-acb5-f0152b5f03c4"
    round_id = "c603d114-5364-4474-a0c4-c41cbf4d3bbd"


    @task
    def get_search_assessments(self):
        """
        Performance test for GET /application_overview/{fund_id}/{round_id} that expects a 200
        """
        with self.client.get(f"/application_overviews/{self.fund_id}/{self.round_id}", catch_response=True) as response:
            check_expected_status(response, 200)

    @task
    def get_metrics(self):
        """
        Performance test for GET /assessments/get-stats/{fund_id}/{round_id} assessment stats that expects a 200
        """
        with self.client.get(f"/assessments/get-stats/{self.fund_id}/{self.round_id}", catch_response=True) as response:
            check_expected_status(response, 200)

    