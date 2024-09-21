class TestOutputFormatter:
    @staticmethod
    def format_success(test_name):
        return f"{test_name}: OK"

    @staticmethod
    def format_failure(test_name, exception_message):
        return f"{test_name}: FAIL - {exception_message}"

    @staticmethod
    def format_skipped(test_name, reason):
        return f"{test_name}: SKIPPED - {reason}"

    @staticmethod
    def format_expected_failure(test_name):
        return f"{test_name}: EXPECTED FAILURE"
