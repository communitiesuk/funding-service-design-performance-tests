def check_expected_status(response, expected_result):
    """
    Function to check if status code is as expected and fail if not
    """
    if response.status_code != expected_result:
        response.failure(
            f"Expected status: {str(expected_result)}"
            + f" Actual: {str(response.status_code)}"
        )
