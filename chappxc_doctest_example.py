"""A simple program to demo doctest.

One way to test this program is to go to cwd,
py -3 -m doctest -v chappxc_doctest_example.py
"""


def is_prime(x):
    """Returns True if a number is a prime number.
    >>> is_prime(1000)
    False
    >>> is_prime(37)
    True
    >>> is_prime(63)
    True
    """
    return not any(x//i == x/i for i in range(x-1, 1, -1))
