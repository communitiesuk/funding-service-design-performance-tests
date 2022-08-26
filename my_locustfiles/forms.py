import json

from common.common_methods import check_expected_status
from common.config import FORMS
from locust import HttpUser
from locust import task

class Forms(HttpUser):

    host = FORMS

# Click new application and tasklist
    @task
    def get_organisation_information(self):
        """
        Performance test for GET new application that expects a 200
        """
        with self.client.get(
            "/organisation-information/about-your-organisation", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)

    @task
    def get_project_information(self):
        """
        Performance test for GET project information that expects a 200
        """
        with self.client.get(
            "/project-information/about-your-project", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_community_use(self):
        """
        Performance test for GET community use that expects a 200
        """
        with self.client.get(
            "/community-use/strategic-case-aMRtTs", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_funding_required(self):
        """
        Performance test for GET funding required that expects a 200
        """
        with self.client.get(
            "/funding-required/management-case", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_community_benefits(self):
        """
        Performance test for GET community benefits that expects a 200
        """
        with self.client.get(
            "/community-benefits/potential-to-deliver-community-benefits-rofqAG", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_value_to_the_community(self):
        """
        Performance test for GET value to the communityu that expects a 200
        """
        with self.client.get(
            "/value-to-the-community/added-value-to-the-community-XXYtSd", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_project_qualification(self):
        """
        Performance test for GET project qualification that expects a 200
        """
        with self.client.get(
            "/project-qualification/subsidy-control-and-state-aid-XQBpkr", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    @task
    def get_declaration(self):
        """
        Performance test for GET declarations that expects a 200
        """
        with self.client.get(
            "/declarations/declarations-YcIHbL", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    
    
  