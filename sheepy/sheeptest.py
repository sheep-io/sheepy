
class SheepyTestCase:
    
    def setUp(self):

        
        self._resources = []  

    def tearDown(self):

        
        for resource in self._resources:
            resource.close()  
        self._resources.clear()

    def run(self):
       
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


    
    def assertEqual(self, first, second, msg=None):
        
        if first != second:
            message = msg or f'{first} != {second}'
            raise AssertionError(message)

    def assertNotEqual(self, first, second, msg=None):
        
        if first == second:
            message = msg or f'{first} == {second}'
            raise AssertionError(message)

    def assertTrue(self, expr, msg=None):
        
        if not expr:
            message = msg or 'The expression is not true'
            raise AssertionError(message)

    def assertFalse(self, expr, msg=None):
        
        if expr:
            message = msg or 'The expression is not false'
            raise AssertionError(message)

    def assertRaises(self, exception, func, *args, **kwargs):
        
        try:
            func(*args, **kwargs)
        except exception:
            return
        except Exception as e:
            raise AssertionError(f'Unexpected exception raised: {e}')
        raise AssertionError(f'{exception.__name__} was not raised')

    

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
