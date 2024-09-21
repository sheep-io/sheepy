from .sheepy import SheepyTestCase
from .sheepy.core.test_suite import TestSuite
from .sheepy.core.test_runner import TestRunner
from .sheepy.core.logger import TestLogger

class ExampleTest(SheepyTestCase):
    def test_success(self):
        self.assertTrue(True)

    def test_failure(self):
        self.assertEqual(1, 2)

    def test_error(self):
        raise Exception("Forced error")

    @SheepyTestCase.skip("Reason to ignore")
    def test_skipped(self):
        pass

    @SheepyTestCase.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 2)


suite = TestSuite([ExampleTest])
runner = TestRunner(suite)
runner.run()