import json

from common.common_methods import check_expected_status
from common.config import FRONTEND
from locust import HttpUser
from locust import task

class FrontEnd(HttpUser):

    host = FRONTEND
   

    @task
    def get_start_page(self):
        """
        Performance test for GET start page that expects a 200
        """
        with self.client.get(
            "", headers={"Authorization":"Basic ZnNkOmZzZA=="}, catch_response=True
        ) as response:
            check_expected_status(response, 200)