class Common:
    def check_expected_status(response, expected_result):
        if response.status_code != expected_result:
            response.failure(
                f"Expected status: {str(expected_result)}"
                + f" Actual: {str(response.status_code)}"
            )
