from .core.__tcases import test_cases
from .utils.formatter import TestOutputFormatter
from .utils.asserts import AssertMethods

class SheepyTestCase(AssertMethods):

    """Base class for test cases.

    This class provides a framework for writing and running unit tests. It includes methods for setting up and tearing down test environments, running tests, and formatting test results.

    Attributes:
        _resources: A list of resources that need to be closed after a test is completed.
    """
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        test_cases.append(cls)
        instance = cls()
        results = instance.run_tests()
        cls._output_results(results)

    def setUp(self):
        self._resources = []

    def tearDown(self):
        for resource in self._resources:
            resource.close()
        self._resources.clear()

    def run_tests(self):
        methods = dir(self)
        test_methods = [method for method in methods if method.startswith("test_")]
        results = []
        for method_name in test_methods:
            method = getattr(self, method_name)
            try:
                if getattr(method, '_skip', False):
                    results.append((method_name, 'skipped'))
                    continue
                self.setUp()
                method()
                self.tearDown()
                results.append((method_name, 'pass'))
            except Exception as e:
                if getattr(method, '_expected_failure', False):
                    results.append((method_name, 'expected failure'))
                else:
                    results.append((method_name, f'fail: {str(e)}'))
        return results

    @classmethod
    def _output_results(cls, results):
        print("\nTest Results:")
        for test_name, result in results:
            if result == 'pass':
                print(TestOutputFormatter.format_success(f"{cls.__name__}.{test_name}"))
            elif result == 'expected failure':
                print(TestOutputFormatter.format_expected_failure(f"{cls.__name__}.{test_name}"))
            elif result.startswith('fail'):
                error_message = result.split(": ", 1)[1]
                print(TestOutputFormatter.format_failure(f"{cls.__name__}.{test_name}", error_message))
            elif result == 'skipped':
                print(TestOutputFormatter.format_skipped(f"{cls.__name__}.{test_name}", getattr(cls, '_skip_reason', '')))

    @staticmethod
    def skip(reason=""):
        def decorator(func):
            func._skip = True
            func._skip_reason = reason
            return func
        return decorator

    @staticmethod
    def expectedFailure(func):
        func._expected_failure = True
        return func
