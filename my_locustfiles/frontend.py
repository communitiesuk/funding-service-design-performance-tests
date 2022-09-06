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
            "/account", headers={"cookie": "eyJjc3JmX3Rva2VuIjoiMGZiNzQyYjkxZTkwYmFjNWIyMmQ3NzBjNDZiNjIxNzI2MjRhMDM4NyJ9.YwjnXw._QiVXgbFx4GDY_f1RbOkl1mBbAI; fsd_user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhY2NvdW50SWQiOiJjYTNjZTQzZS1kYWZiLTRlNTktOTczNC0xZjA3YzgwM2U2ZWQiLCJpYXQiOjE2NjI0NzEwMDcsImV4cCI6MTY2MjU1NzQwN30.hsxal2POsyzvwGI66Yqr9wZ7AdFIiukdmuqXHzzdFciWdToq0GfHucEcn9RAGKyBvxwOG87LGSEOOr75OG8Afc_UxjstTznMMivxUJQvtIqarCEtnLvnUiQc1RRdAP_v_xQObEtqaGf9JvvAqAXMQAXRBBBbmAbn97hqPWIqRrVrHu1GybKTY_Rxq65YhLELoHepXVidmLdse2nsBtCmjKt_hlqNeA1o73vHOJ0t5yvR-XABGdNfDtNaI7o7rGhjKkBHf8pqGPl2Q3QKi5XOnNOrC6ono3LdAi6VMit34KTlzmLziLubQDH2yiTYd61H4gryDrrPKvhf5QorhwZS7ydE8ZhWwTLJ3R5XYZ8vACSGY0DS2crAhKxQBhJl_gHGKU7myq759LmhQPt8MPR5IyDUCyA9ktJgdjRMdfEWKEuznksuVB7ZtQDnVpws5oi3KRQv4rcDsDbtNNlNP7ScXxdIRftUnZrQSfDHG6SHkdDXi-CJ_kTl-UXci_BYtnLBv7dL2yNA9ZmvgqPWSz9_Hz-WFO4oV9Ypqj15kaUG8bzN5UlveIrVxZoZzBjHOI9HYWc-1_j8dGTFxNoxMUC2FH-wYyUpVBKnmnT3evIJDux1tbo0V64fEWpHqJWbC9DkpUURrgTVJaj2tEExDBTkKK_PsgyKJXAKbZA4nf--4iY"}, catch_response=True
        ) as response:
            check_expected_status(response, 200)

    # Click new application and tasklist
    @task
    def get_new_application(self):
        """
        Performance test for GET new application that expects a 200
        """
        with self.client.get(
            "/tasklist/29080057-c2e4-4a99-95e6-afd63f72dae5", catch_response=True
        ) as response:
            check_expected_status(response, 200)
    
    # Submit application
    @task
    def submit_application(self):
        """
        Performance test for POST submit application that expects a 200
        """
        with self.client.post(
            "/submit_application", headers={"cookie": "session_cookie=eyJjc3JmX3Rva2VuIjoiMGZiNzQyYjkxZTkwYmFjNWIyMmQ3NzBjNDZiNjIxNzI2MjRhMDM4NyJ9.YwjnXw._QiVXgbFx4GDY_f1RbOkl1mBbAI; fsd_user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhY2NvdW50SWQiOiJjYTNjZTQzZS1kYWZiLTRlNTktOTczNC0xZjA3YzgwM2U2ZWQiLCJpYXQiOjE2NjI0NzEwMDcsImV4cCI6MTY2MjU1NzQwN30.hsxal2POsyzvwGI66Yqr9wZ7AdFIiukdmuqXHzzdFciWdToq0GfHucEcn9RAGKyBvxwOG87LGSEOOr75OG8Afc_UxjstTznMMivxUJQvtIqarCEtnLvnUiQc1RRdAP_v_xQObEtqaGf9JvvAqAXMQAXRBBBbmAbn97hqPWIqRrVrHu1GybKTY_Rxq65YhLELoHepXVidmLdse2nsBtCmjKt_hlqNeA1o73vHOJ0t5yvR-XABGdNfDtNaI7o7rGhjKkBHf8pqGPl2Q3QKi5XOnNOrC6ono3LdAi6VMit34KTlzmLziLubQDH2yiTYd61H4gryDrrPKvhf5QorhwZS7ydE8ZhWwTLJ3R5XYZ8vACSGY0DS2crAhKxQBhJl_gHGKU7myq759LmhQPt8MPR5IyDUCyA9ktJgdjRMdfEWKEuznksuVB7ZtQDnVpws5oi3KRQv4rcDsDbtNNlNP7ScXxdIRftUnZrQSfDHG6SHkdDXi-CJ_kTl-UXci_BYtnLBv7dL2yNA9ZmvgqPWSz9_Hz-WFO4oV9Ypqj15kaUG8bzN5UlveIrVxZoZzBjHOI9HYWc-1_j8dGTFxNoxMUC2FH-wYyUpVBKnmnT3evIJDux1tbo0V64fEWpHqJWbC9DkpUURrgTVJaj2tEExDBTkKK_PsgyKJXAKbZA4nf--4iY", "referer":"https://frontend.uat.gids.dev/tasklist/29080057-c2e4-4a99-95e6-afd63f72dae5"},
            catch_response=True
        ) as response:
            check_expected_status(response, 200)