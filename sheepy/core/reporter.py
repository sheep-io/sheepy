class TestReporter:
    @staticmethod
    def generate_report(results):
        print("\nTest Results:")
        for test_name, result in results:
            print(f"{test_name}: {result}")
