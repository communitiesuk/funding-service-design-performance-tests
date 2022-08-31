import json

from common.common_methods import check_expected_status
from common.config import FRONTEND
from locust import HttpUser
from locust import task

class FrontEnd(HttpUser):

    host = FRONTEND
   
    # Start page
    @task
    def get_start_page(self):
        """
        Performance test for GET start page that expects a 200
        """
        with self.client.get(
            "", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    # Applicant dashboard (401)
    @task
    def get_applicant_dashboard(self):
        """
        Performance test for GET applicant dashboard that expects a 200
        """
        with self.client.get(
            "/account", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # Click new application and tasklist
    @task
    def get_new_application(self):
        """
        Performance test for GET new application that expects a 200
        """
        with self.client.get(
            "/tasklist/d0b7e173-6690-4f0a-86f2-904810d7eb5d", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    # Submit application
    @task
    def submit_application(self):
        """
        Performance test for GET submit application that expects a 200
        """
        with self.client.post(
            "/submit_application", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    