import inspect

class TestSuite:
    def __init__(self, test_cases):

        self.test_cases = test_cases

    def get_tests(self):

        tests = []
        for test_case_class in self.test_cases:
            test_case_instance = test_case_class()  
            methods = inspect.getmembers(test_case_instance, predicate=inspect.ismethod)
            test_methods = [method for name, method in methods if name.startswith("test_")]
            tests.extend([(test_case_instance, method) for method in test_methods])
        return tests
