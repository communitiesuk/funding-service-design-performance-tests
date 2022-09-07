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
            "", catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    # Applicant dashboard
    @task
    def get_applicant_dashboard(self):
        """
        Performance test for GET applicant dashboard that expects a 200
        """
        with self.client.get(
            "/account", headers={"cookie": "session_cookie=eyJjc3JmX3Rva2VuIjoiMzQ0MWM1OWYyODlkMWJlMjUyZWVkYmQ4NWJhNTU5YWFhYzExOGQyYyJ9.Yw3hBg.W2E7Kq5gg3eKOgdaSuRjBUBiFIY; fsd_user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhY2NvdW50SWQiOiI5YTFlNGEwZi0zZjA2LTRkNzQtOWRmOC01NjI0ZTU0N2NmN2QiLCJpYXQiOjE2NjI1NTY5MTYsImV4cCI6MTY2MjY0MzMxNn0.Pj6Ub6apIy7V1cF6a0fhEEFoF-XyvAavwR_dL11Cm2g4xOk6x25ow6GohjYFbEZmLnTEtJlHMoNlfoXZVvauxg6udYyS6NEwJPP99ppzjjZkAylXFEA7AXmRlui3gOotefPEDLzL_2fpXvnfrJcPw1o8h4RLd6bq2kwxQu7Obg0"}, catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # Click new application and tasklist
    @task
    def get_new_application(self):
        """
        Performance test for GET new application that expects a 200
        """
        with self.client.get(
            "/tasklist/baec9d16-e34d-4242-9fb9-67255d936ce9",headers={"cookie": "session_cookie=eyJjc3JmX3Rva2VuIjoiMzQ0MWM1OWYyODlkMWJlMjUyZWVkYmQ4NWJhNTU5YWFhYzExOGQyYyJ9.Yw3hBg.W2E7Kq5gg3eKOgdaSuRjBUBiFIY; fsd_user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhY2NvdW50SWQiOiI5YTFlNGEwZi0zZjA2LTRkNzQtOWRmOC01NjI0ZTU0N2NmN2QiLCJpYXQiOjE2NjI1NTY5MTYsImV4cCI6MTY2MjY0MzMxNn0.Pj6Ub6apIy7V1cF6a0fhEEFoF-XyvAavwR_dL11Cm2g4xOk6x25ow6GohjYFbEZmLnTEtJlHMoNlfoXZVvauxg6udYyS6NEwJPP99ppzjjZkAylXFEA7AXmRlui3gOotefPEDLzL_2fpXvnfrJcPw1o8h4RLd6bq2kwxQu7Obg0"}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    # Submit application
    @task
    def submit_application(self):
        """
        Performance test for POST submit application that expects a 200
        """
        with self.client.post(
            "/submit_application", headers={"cookie": 
            "session_cookie=eyJjc3JmX3Rva2VuIjoiMzQ0MWM1OWYyODlkMWJlMjUyZWVkYmQ4NWJhNTU5YWFhYzExOGQyYyJ9.Yw3hBg.W2E7Kq5gg3eKOgdaSuRjBUBiFIY; fsd_user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhY2NvdW50SWQiOiI5YTFlNGEwZi0zZjA2LTRkNzQtOWRmOC01NjI0ZTU0N2NmN2QiLCJpYXQiOjE2NjI1NTY5MTYsImV4cCI6MTY2MjY0MzMxNn0.Pj6Ub6apIy7V1cF6a0fhEEFoF-XyvAavwR_dL11Cm2g4xOk6x25ow6GohjYFbEZmLnTEtJlHMoNlfoXZVvauxg6udYyS6NEwJPP99ppzjjZkAylXFEA7AXmRlui3gOotefPEDLzL_2fpXvnfrJcPw1o8h4RLd6bq2kwxQu7Obg0", 
            "referer":"https://frontend.dev.gids.dev/tasklist/baec9d16-e34d-4242-9fb9-67255d936ce9"},
            catch_response=True
        ) as response:
            check_expected_status(response, 200)