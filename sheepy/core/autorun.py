from .runner import TestRunner
from ..collector import collect_test_cases

def auto_run():
    test_cases = collect_test_cases()  
    if test_cases:
        runner = TestRunner(test_cases)
        runner.run()


auto_run()
