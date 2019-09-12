"""A simpler program I found on YouTube about asyncio.

https://osf.io/w8u26/"""

import asyncio
import time


def is_prime(x):
    """Returns True if a number is a prime number."""
    return not any(x//i == x/i for i in range(x-1, 1, -1))


# Function without asyncio
def highest_prime_below1(x):
    """Find the highest prime number below x."""
    print('Highest prime below', x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('Highest prime below {}: {}'.format(x, y))
            return y
        time.sleep(0.01)
    return None


# Function with asyncio
async def highest_prime_below2(x):
    """Find the highest prime number below x."""
    print('Highest prime below', x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('Highest prime below {}: {}'.format(x, y))
            return y
        await asyncio.sleep(0.01)           # Suspends temporarily to give other async functions a chance to execute
    return None


# Program without asyncio
def main1():
    highest_prime_below1(100000)
    highest_prime_below1(10000)
    highest_prime_below1(1000)
    print()
main1()


# Program with asyncio
async def main2():
    await asyncio.wait([highest_prime_below2(100000),
                        highest_prime_below2(10000),
                        highest_prime_below2(1000)])

loop = asyncio.get_event_loop()
loop.run_until_complete(main2())
loop.close()
