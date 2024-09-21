import inspect
from functools import wraps

def sheepy(func):
    func._is_test = True

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
