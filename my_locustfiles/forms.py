import json

from common.common_methods import check_expected_status
from common.config import FORMS
from locust import HttpUser
from locust import task

class Forms(HttpUser):

    host = FORMS

# Complete tasks from tasklist
    
    # 1. About Your Organisation
    # Form: Organisation Information
    @task
    def get_organisation_information(self):
        """
        Performance test for GET new application that expects a 200
        """
        with self.client.get(
            "/organisation-information/summary", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # 2. About Your Project
    # Form: Project Information
    @task
    def get_project_information(self):
        """
        Performance test for GET project information that expects a 200
        """
        with self.client.get(
            "/project-information/summary", catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    # 3.Strategic Case
    # Form: Community use
    @task
    def get_community_use(self):
        """
        Performance test for GET community use that expects a 200
        """
        with self.client.get(
            "/community-use/summary", catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    # 4.Management Case
    # Form: Funding required
    @task
    def get_funding_required(self):
        """
        Performance test for GET funding required that expects a 200
        """
        with self.client.get(
            "/funding-required/summary", catch_response=True
        ) as response:
            check_expected_status(response, 200)
    

    # 5.Potential To Deliver Community Benefits
    # Form: Community Benefits
    @task
    def get_community_benefits(self):
        """
        Performance test for GET community benefits that expects a 200
        """
        with self.client.get(
            "/community-benefits/summary", catch_response=True
        ) as response:
            check_expected_status(response, 200)
    

    # 6.Added Value To Community
    # Form: Value To The Community
    @task
    def get_value_to_the_community(self):
        """
        Performance test for GET value to the community that expects a 200
        """
        with self.client.get(
            "/value-to-the-community/summary", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # 7.Subsidy Control / State Aid
    # Form: Project Qualification
    @task
    def get_project_qualification(self):
        """
        Performance test for GET project qualification that expects a 200
        """
        with self.client.get(
            "/project-qualification/summary", catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # 8.Check Declarations
    # Form: Declarations
    @task
    def get_declaration(self):
        """
        Performance test for GET declarations that expects a 200
        """
        with self.client.get(
            "/declarations/summary", catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    
    
