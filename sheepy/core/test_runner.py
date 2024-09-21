from .reporter import TestReporter
from .logger import TestLogger

class TestRunner:
    def __init__(self, suite, logger=None):
        self.suite = suite
        self.logger = logger or TestLogger()
        self.reporter = TestReporter()

    def run(self):

        tests = self.suite.get_tests()  
        results = []
        
        for test_case, test_method in tests:
            test_name = f"{test_case.__class__.__name__}.{test_method.__name__}"
            try:
                self.logger.log(f"Running test: {test_name}")
                test_case.setUp()   
                test_method()       
                test_case.tearDown()  
                results.append((test_name, 'pass'))
            except Exception as e:
                results.append((test_name, f'fail: {str(e)}'))

        
        self.reporter.generate_report(results)
        for test_name, result in results:
            self.logger.log(f"{test_name}: {result}")
