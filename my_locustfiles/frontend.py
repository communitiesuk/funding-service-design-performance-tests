import json

from common.common_methods import check_expected_status
from common.config import FRONTEND
from locust import HttpUser
from locust import task

class FrontEnd(HttpUser):

    host = FRONTEND
    new_application_json_file = open(
        "./data/application_store/new_application.json", "r"
    )
    new_application_json = json.loads(new_application_json_file.read())
   
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
            "/account", headers={"cookie": "session_cookie=eyJjc3JmX3Rva2VuIjoiMGZiNzQyYjkxZTkwYmFjNWIyMmQ3NzBjNDZiNjIxNzI2MjRhMDM4NyJ9.YwjnXw._QiVXgbFx4GDY_f1RbOkl1mBbAI; fsd_user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhY2NvdW50SWQiOiJjYTNjZTQzZS1kYWZiLTRlNTktOTczNC0xZjA3YzgwM2U2ZWQiLCJpYXQiOjE2NjIzODE3MzAsImV4cCI6MTY2MjQ2ODEzMH0.h3vWpDKjNdMWtEPA68VLEZGkhuwgS-jA3UcDFub_u6PQ9UL5d0lrmKEpx_gLmi2KbOvcnqYLeq2Hw-5HcRUre5P3oaRaHzIUQj00nIYDlFhNZ-pjeJ14Q387F6Zq2m3hJ722Jyo_Wc1hMpkHOXAD0aE7uts9HHP90yZGjw2up1e6u1JWFxwLAtWvgzlVaz6C8Yeu-udcRmf94IwflFe8NA-Es3n1QE4EN8tb1ejOBk-gmYfySe04czhTmkhMEsrwlJZaJAE5qbPIHpv1UaDaS6QwLpUq3GXTRkl2dCOhmWJ9BZPcbBUTR2x-VD9HspN39pv-Yl4yEZYT_338z1RUjVlcKOMn1jDnp4Hmiv5rNFUdJ_YL0A9nMXHUEisR7QhgLHthbYaiVgnjWiXi7HbvWH_mzNBwMqpcQ4KNdPLszJsvUgzDRUYeGu7kyyzhSHOdaNsDIgrcybVz0wggkd1v4Yvq5wu2BeCcYGV4WYLCpNb3WHEdfYjz0aX748Nvx-CuYm779lZhd5Xhu5RkxB-hN07g6Owr7V5NstqLEEUd1d5xQ7jB_YPIhrz2oL5ynmikQcLNB3hRTnDQw7-Ypmtq2NTMa0Rl8vFM7iJrrDHISZN5m7R4r3mix-03zdIQG8mC0k5EeveZjZ6XadKmkcN1-z8AEfEt5usVfUAcNDfNqtQ"}, catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # Click new application and tasklist
    @task
    def get_new_application(self):
        """
        Performance test for GET new application that expects a 200
        """
        with self.client.get(
            "/tasklist/8f8ac7e7-5eea-4a47-8792-0c9d6a04c75c", catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    # Submit application
    @task
    def submit_application(self):
        """
        Performance test for POST submit application that expects a 200
        """
        with self.client.post(
            "/submit_application", 
            json=self.new_application_json,
            catch_response=True
        ) as response:
            check_expected_status(response, 200)