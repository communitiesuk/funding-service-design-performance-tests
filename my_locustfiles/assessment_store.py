import json

from common.common_methods import check_expected_status
from common.config import ASSESSMENT_STORE
from locust import HttpUser
from locust import task

class AssessmentStore(HttpUser):
    host = ASSESSMENT_STORE
    assessment_id = 1


    @task
    def list_all_asessments(self):
        """
        Performance test for GET /assessments that expects a 200
        """
        with self.client.get("/assessments", catch_response=True) as response:
            check_expected_status(response, 200)

    @task
    def get_scores(self):
        """
        Performance test for GET /assessments/{assessment_id}/scores that expects a 200
        """
        with self.client.get(f"/assessments/{self.assessment_id}/scores", catch_response=True) as response:
            check_expected_status(response, 200)

    