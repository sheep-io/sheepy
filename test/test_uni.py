from sheepy.sheeptest import SheepyTestCase

class ExampleTest(SheepyTestCase):

    """Expected output

    Test Results:
        ExampleTest.test_error: FAIL - Forced error
        ExampleTest.test_expected_failure: EXPECTED FAILURE
        ExampleTest.test_failure: FAIL - 1 != 2
        ExampleTest.test_skipped: SKIPPED -
        ExampleTest.test_success: OK
    """

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

