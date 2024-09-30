from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, '_debug_results'):
            self._debug_results = []
        
        test_name = f"{self.__class__.__name__}.{func.__name__}"
        
        try:
            
            func(self, *args, **kwargs)
            
            self._debug_results.append((test_name, 'pass'))
        
        except Exception as e:
            
            self._debug_results.append((test_name, f'fail: {str(e)}'))
            
            print("\nDebug Report (so far):")
            for result in self._debug_results:
                print(f"{result[0]}: {result[1]}")
            
            
            user_input = input("\nDo you want to continue with the next test? (y/n): ").strip().lower()
            if user_input != 'y':
                print("\nTest execution stopped.")
                raise  

        finally:
            
            if hasattr(self, '_debug_results'):
                print("\nCurrent Test Results:")
                for result in self._debug_results:
                    print(f"{result[0]}: {result[1]}")
    return wrapper
