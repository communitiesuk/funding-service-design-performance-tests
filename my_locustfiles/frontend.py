import json

from common.common_methods import check_expected_status
from common.config import FRONTEND
from locust import HttpUser
from locust import task
from locust import between

class FrontEnd(HttpUser):

  
    wait_time = between(30, 60)
    host = FRONTEND
   
    # Start page
    @task()
    def get_start_page(self):
        """
        Performance test for GET start page that expects a 200
        """
        with self.client.get(
            "", catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    # Applicant dashboard
    @task()
    def get_applicant_dashboard(self):
        """
        Performance test for GET applicant dashboard that expects a 200
        """
        with self.client.get(
            "/account", headers={"cookie": "session_cookie=eyJjc3JmX3Rva2VuIjoiMzQ0MWM1OWYyODlkMWJlMjUyZWVkYmQ4NWJhNTU5YWFhYzExOGQyYyJ9.Yw3hBg.W2E7Kq5gg3eKOgdaSuRjBUBiFIY; fsd_user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhY2NvdW50SWQiOiI5YTFlNGEwZi0zZjA2LTRkNzQtOWRmOC01NjI0ZTU0N2NmN2QiLCJpYXQiOjE2NjI5NzI1NTcsImV4cCI6MTY2MzA1ODk1N30.JGfiWv7LNN0ZVzZGUj8aSWROtM6IpWVI_xDI2uDRntvfr3A_oxOekLg6Nxa5RvUf1YSsF4fCBXqLl2XnF41OMAzcTtny0OHXHKRxKqXbujaIZMMPiWJiwUuWCOVhYrac9uXt5IR75ZmtVBN65H7fHFxq03sVRAQuMVHXGjAxr1g"}, catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # Click new application and tasklist
    @task()
    def get_new_application(self):
        """
        Performance test for GET new application that expects a 200
        """
        with self.client.get(
            "/tasklist/dfa16c14-f6d0-4f8b-83a4-bb0f4badb03b",headers={"cookie": "'session_cookie=eyJjc3JmX3Rva2VuIjoiMzQ0MWM1OWYyODlkMWJlMjUyZWVkYmQ4NWJhNTU5YWFhYzExOGQyYyJ9.Yw3hBg.W2E7Kq5gg3eKOgdaSuRjBUBiFIY; fsd_user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhY2NvdW50SWQiOiI5YTFlNGEwZi0zZjA2LTRkNzQtOWRmOC01NjI0ZTU0N2NmN2QiLCJpYXQiOjE2NjI5NzI1NTcsImV4cCI6MTY2MzA1ODk1N30.JGfiWv7LNN0ZVzZGUj8aSWROtM6IpWVI_xDI2uDRntvfr3A_oxOekLg6Nxa5RvUf1YSsF4fCBXqLl2XnF41OMAzcTtny0OHXHKRxKqXbujaIZMMPiWJiwUuWCOVhYrac9uXt5IR75ZmtVBN65H7fHFxq03sVRAQuMVHXGjAxr1g'"}, catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    # Submit application
    @task(1)
    def submit_application(self):
        """
        Performance test for POST submit application that expects a 200
        """
        with self.client.post(
            "/submit_application", headers={"cookie": 
            "session_cookie=eyJjc3JmX3Rva2VuIjoiMzQ0MWM1OWYyODlkMWJlMjUyZWVkYmQ4NWJhNTU5YWFhYzExOGQyYyJ9.Yw3hBg.W2E7Kq5gg3eKOgdaSuRjBUBiFIY; fsd_user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhY2NvdW50SWQiOiI1ZmEwMzFkMi1jOTk4LTRmOTktYmFkMy04M2Y5NGZmYTJiNGQiLCJpYXQiOjE2NjMwNjM2MTAsImV4cCI6MTY2MzE1MDAxMH0.OgknMN2y5cyv0cnNRBdX8fUW1Gi5YaaAF13N6Wo2V-XTJErnxNs8bZaP-9QpzAYbcB3WnIquHxijXq3h899a8W2PrXW2qU1Jr7NzjodsmJJxOrXczAkxwGT0SpaR5KeFVJrDYJbdKeUbbeCkT61AFtZhVp609PyVywyTXXXBldE", 
            "referer":"https://frontend.dev.gids.dev/tasklist/dfa16c14-f6d0-4f8b-83a4-bb0f4badb03b"},
            catch_response=True
        ) as response:
            check_expected_status(response, 200)