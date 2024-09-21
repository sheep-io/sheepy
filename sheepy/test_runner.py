from reporter import TestReporter
from logger import TestLogger

class TestRunner:
    def __init__(self, suite, logger=None):
        self.suite = suite
        self.logger = logger or TestLogger()
        self.reporter = TestReporter()

    def run_tests(self):
        results = []
        for test in self.suite.get_tests():
            try:
                self.logger.log(f"Running test: {test.__name__}")
                test()
                results.append((test.__name__, 'pass'))
            except Exception as e:
                results.append((test.__name__, f'fail: {str(e)}'))
        return results
