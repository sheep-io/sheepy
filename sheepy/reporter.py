class TestReporter:
    @staticmethod
    def generate_report(results):
        print("Test Results:")
        for test_name, result in results:
            print(f"{test_name}: {result}")
