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