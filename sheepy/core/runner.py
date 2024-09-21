from .indexer import TestIndexer
from .reporter import TestReporter
from .logger import TestLogger

class TestRunner:
    def __init__(self, test_cases=None, logger=None):
        self.indexer = TestIndexer()
        self.logger = logger or TestLogger()
        self.reporter = TestReporter()

        
        if test_cases:
            for test_case in test_cases:
                self.indexer.add_test_methods(test_case)

    def run(self):
        if self.indexer.has_tests():
            tests = self.indexer.get_tests()
            results = []

            for test_case, test_method in tests:
                test_name = f"{test_case.__class__.__name__}.{test_method}"
                try:
                    self.logger.log(f"Running test: {test_name}")
                    test_case.setUp()
                    getattr(test_case, test_method)()
                    test_case.tearDown()
                    results.append((test_name, 'pass'))
                except Exception as e:
                    results.append((test_name, f'fail: {str(e)}'))

            self.reporter.generate_report(results)
            for test_name, result in results:
                self.logger.log(f"{test_name}: {result}")
