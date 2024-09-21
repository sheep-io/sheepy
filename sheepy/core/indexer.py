import inspect
from bisect import bisect_left

class TestIndexer:
    def __init__(self):
        self.test_index = []

    def add_test_methods(self, test_case):
        test_methods = inspect.getmembers(test_case, predicate=inspect.ismethod)
        test_names = [name for name, method in test_methods if name.startswith("test_")]
        for test_name in test_names:
            bisect_left(self.test_index, (test_case, test_name))  

    def has_tests(self):
        
        return len(self.test_index) > 0

    def get_tests(self):
    
        return self.test_index
