class AssertMethods:
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
