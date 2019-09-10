"""A handy template for creating decorators! Also refer to ch10_decor_checklogin.py"""
from functools import wraps
# Any other imports required.


def decorator_name(func: object) -> object:
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Code to execute BEFORE calling the decorated function

        # 2. Call the decorated function, as required, returning it's results if needed
            return func(*args, **kwargs)

        # 3. Code to execute INSTEAD of calling the decorated function

    return wrapper


"""The 4 requirements for a decorator:
1. Is a function.
2. Takes the decorated function as an argument.
3. Returns a new function.
4. Maintains the decorated function's signature.

When creating your own decorators, always import, then use, 
the 'functools' module’s 'wraps' function.
"""
