from .core.__tcases import test_cases
from .sheeptest import SheepyTestCase
import sys
import inspect

def collect_test_cases():
    current_module = sys.modules[__name__]

    for name, obj in inspect.getmembers(current_module, inspect.isclass):
        if issubclass(obj, SheepyTestCase) and obj is not SheepyTestCase:
            test_cases.append(obj())
            print(f"Found test case: {obj.__name__}")
            
    return test_cases
