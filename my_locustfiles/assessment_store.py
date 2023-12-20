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
    def get_assessment_stats(self):
        """
        Performance test for GET /assessments/get-stats/{fund_id}/{round_id} assessment stats that expects a 200
        """
        with self.client.get(f"/assessments/get-stats/{self.fund_id}/{self.round_id}",
        headers={"User-Agent": USER_AGENT},
        catch_response=True,
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_team_flagging_stats(self):
        """
        Performance test for GET /assessments/get-team-flag-stats/{fund_id}/{round_id} team flagging stats that expects a 200
        """
        with self.client.get(f"/assessments/get-team-flag-stats/{self.fund_id}/{self.round_id}",
        headers={"User-Agent": USER_AGENT},
        catch_response=True,
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_tags_associated_with_fund_and_round(self):
        """
        Performance test for GET /funds/{fund_id}/rounds/{round_id}/tags tags associated with fund and round that expects a 200
        """
        with self.client.get(f"/funds/{self.fund_id}/rounds/{self.round_id}/tags",
        headers={"User-Agent": USER_AGENT},
        catch_response=True,
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_all_tag_types(self):
        """
        Performance test for GET /tag_types tag types that expects a 200
        """
        with self.client.get("/tag_types",
        headers={"User-Agent": USER_AGENT},
        catch_response=True,
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_all_assessments_for_export(self):
        """
        Performance test for GET /application_fields_export/{fund_id}/{round_id}/{report_type} assessments for export that expects a 200
        """
        with self.client.get(f"/application_fields_export/{self.fund_id}/{self.round_id}/ASSESSOR_EXPORT",
        headers={"User-Agent": USER_AGENT},
        catch_response=True,
        ) as response:
            check_expected_status(response, 200)



    