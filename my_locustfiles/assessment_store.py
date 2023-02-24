import json

from common.common_methods import check_expected_status
from common.config import ASSESSMENT_STORE
from common.config import FUND_ID
from common.config import ROUND_ID
from common.config import USER_AGENT
from locust import HttpUser
from locust import task

class AssessmentStore(HttpUser):
    host = ASSESSMENT_STORE
    fund_id = FUND_ID
    round_id = ROUND_ID


    @task
    def get_search_assessments(self):
        """
        Performance test for GET /application_overview/{fund_id}/{round_id} that expects a 200
        """
        with self.client.get(f"/application_overviews/{self.fund_id}/{self.round_id}",
        headers={"User-Agent": USER_AGENT},
        catch_response=True,
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_metrics(self):
        """
        Performance test for GET /assessments/get-stats/{fund_id}/{round_id} assessment stats that expects a 200
        """
        with self.client.get(f"/assessments/get-stats/{self.fund_id}/{self.round_id}",
        headers={"User-Agent": USER_AGENT},
        catch_response=True,
        ) as response:
            check_expected_status(response, 200)

    