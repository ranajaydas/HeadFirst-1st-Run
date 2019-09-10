"""A simple Login checking decorator (check_logged_in)"""
from flask import session
from functools import wraps


def check_logged_in(func: object) -> object:   # 'func' is the decorated function
    @wraps(func)                               # Decorate the wrapper function (decoratorception!)
    def wrapper(*args, **kwargs):              # Foolproof way of ensuring we maintain the decorated func's signature

        if 'logged-in' in session:

            return func(*args, **kwargs)

        return "You're not logged in, dude."

    return wrapper


"""The 4 requirements for a decorator:
1. Is a function.
2. Takes the decorated function as an argument.
3. Returns a new function.
4. Maintains the decorated function's signature.

When creating your own decorators, always import, then use, 
the 'functools' module’s 'wraps' function.
"""
