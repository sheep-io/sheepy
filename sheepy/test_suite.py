import inspect

class TestSuite:
    def __init__(self, test_cases):
        self.test_cases = test_cases

    def get_tests(self):
        tests = []
        for test_case in self.test_cases:
            
            methods = inspect.getmembers(test_case, predicate=inspect.ismethod)
            
            filtered_methods = [method for name, method in methods if hasattr(method, '_is_test')]
            tests.extend(filtered_methods)
        return tests
