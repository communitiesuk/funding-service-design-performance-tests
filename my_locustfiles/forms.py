import json

from common.common_methods import check_expected_status
from common.config import FORMS
from locust import HttpUser
from locust import task

class Forms(HttpUser):

    host = FORMS
    new_application_json_file = open(
        "./data/forms/organisation-information.json", "r"
    )
    new_application_json = json.loads(new_application_json_file.read())


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
    def post_organisation_information(self):
        """
        Performance test for POST new application and organisation_information that expects a 201
        """
        with self.client.put("/organisation-information/about-your-organisation", json={self.new_application_json}, catch_response=True
        ) as response:
            check_expected_status(response, 201)