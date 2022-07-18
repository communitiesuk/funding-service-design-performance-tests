import json

from common.common_methods import check_expected_status
from common.config import ASSESSMENT_STORE
from locust import HttpUser
from locust import task

class AssessmentStore(HttpUser):
    host = ASSESSMENT_STORE


    @task
    def list_all_asessments(self):
        """
        Performance test for GET /assessments that expects a 200
        """
        with self.client.get("/assessments", catch_response=True) as response:
            check_expected_status(response, 200)

    