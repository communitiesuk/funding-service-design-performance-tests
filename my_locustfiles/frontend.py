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
            "/account", headers={"cookie": "eyJjc3JmX3Rva2VuIjoiMGZiNzQyYjkxZTkwYmFjNWIyMmQ3NzBjNDZiNjIxNzI2MjRhMDM4NyJ9.YwjnXw._QiVXgbFx4GDY_f1RbOkl1mBbAI; fsd_user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhY2NvdW50SWQiOiJjYTNjZTQzZS1kYWZiLTRlNTktOTczNC0xZjA3YzgwM2U2ZWQiLCJpYXQiOjE2NjI1NDA5MDYsImV4cCI6MTY2MjYyNzMwNn0.ILHz1t5N4vzqHuUd1XiYLigL4PpOmZdK_LFL48j5YE7Pwm6SgXy0Iryh2xZw5jR7F4Oa8knjHLWCCjO6J_7eTqGgDMY0Q_GAd_HDb_VtDIyqn1ZoSK9K5AZcmrhAjfaWKo49FGNs42fwCWi0w9oE-RTLr4u1qfuF661X_deXWi1m7dGx9fL0zM-y8N2p-SCHSIdX9a74vM2QYQ3NtSQJc8_lnNF4ZNXQqEW_16TrQ_xEveUpPC0ZUDD1Ljj-PlnwJBeRKx4H9znZEC8Vc-R3kkX4b-sOAixkbXeUIsSz1otaLqWIQbHEy3iLuiZBXpfgSI3-glnd3l6av8ZKNRU43AuDwNpT4zpVQ17s3f3ZG9bhpDCcgL61azMrYh-ceR79q10kxvTA_9Olqa7eUUe5wTnkoQ7n-vuTemUw2NL4DeOqMbPuE2d2pjADEZLk2soz474Fvqy5eZGwMmLnHOD1ZAxLeTCk0lACwV2FeyD0cHWBpry36_deyzJSWxJvRkJT7zjF8rNswgssUcRAzbQjY-Fy776sUsAGyFviG4vLWlaKGBQ6-34ChUIauDuP3NgGb-7IAx_NGPgxAoam-N30zNXqFhgy4WO6BUZX5ZcKQcM3fgHPYSEbrR2089QlB2iLEOBPsI3JsmgHh0FxRIcT_UB7tq9dRC9l3vj-NydTtVA"}, catch_response=True
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
            "/submit_application", headers={"cookie":"session_cookie=eyJjc3JmX3Rva2VuIjoiMGZiNzQyYjkxZTkwYmFjNWIyMmQ3NzBjNDZiNjIxNzI2MjRhMDM4NyJ9.YwjnXw._QiVXgbFx4GDY_f1RbOkl1mBbAI; fsd_user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhY2NvdW50SWQiOiJjYTNjZTQzZS1kYWZiLTRlNTktOTczNC0xZjA3YzgwM2U2ZWQiLCJpYXQiOjE2NjI1NDA5MDYsImV4cCI6MTY2MjYyNzMwNn0.ILHz1t5N4vzqHuUd1XiYLigL4PpOmZdK_LFL48j5YE7Pwm6SgXy0Iryh2xZw5jR7F4Oa8knjHLWCCjO6J_7eTqGgDMY0Q_GAd_HDb_VtDIyqn1ZoSK9K5AZcmrhAjfaWKo49FGNs42fwCWi0w9oE-RTLr4u1qfuF661X_deXWi1m7dGx9fL0zM-y8N2p-SCHSIdX9a74vM2QYQ3NtSQJc8_lnNF4ZNXQqEW_16TrQ_xEveUpPC0ZUDD1Ljj-PlnwJBeRKx4H9znZEC8Vc-R3kkX4b-sOAixkbXeUIsSz1otaLqWIQbHEy3iLuiZBXpfgSI3-glnd3l6av8ZKNRU43AuDwNpT4zpVQ17s3f3ZG9bhpDCcgL61azMrYh-ceR79q10kxvTA_9Olqa7eUUe5wTnkoQ7n-vuTemUw2NL4DeOqMbPuE2d2pjADEZLk2soz474Fvqy5eZGwMmLnHOD1ZAxLeTCk0lACwV2FeyD0cHWBpry36_deyzJSWxJvRkJT7zjF8rNswgssUcRAzbQjY-Fy776sUsAGyFviG4vLWlaKGBQ6-34ChUIauDuP3NgGb-7IAx_NGPgxAoam-N30zNXqFhgy4WO6BUZX5ZcKQcM3fgHPYSEbrR2089QlB2iLEOBPsI3JsmgHh0FxRIcT_UB7tq9dRC9l3vj-NydTtVA", 
            "referer": "https://frontend.uat.gids.dev/tasklist/29080057-c2e4-4a99-95e6-afd63f72dae5"},
            catch_response=True
        ) as response:
            check_expected_status(response, 200)