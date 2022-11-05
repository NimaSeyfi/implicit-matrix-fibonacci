from gmpy2 import mpz
from functools import lru_cache
import time


def multiply(a, b, x, y):
    return x*(a+b) + a*y, a*x + b*y


def square(a, b):
    a2 = a * a
    b2 = b * b
    ab = a * b
    return a2 + (ab << 1), a2 + b2


@lru_cache(100)
def dynamic_repeated_squares(a, b, n):
    # n must be a power of two.
    if n == 0:
        return (0, 1)
    elif n == 1:
        return (a, b)
    return square(*dynamic_repeated_squares(a, b, n // 2))


def dynamic_power(a, b, m):
    if m == 0:
        return (0, 1)
    elif m == 1:
        return (a, b)
    else:
        n = 2
        while n <= m:
            n = n * 2
        n = n // 2
        x, y = dynamic_repeated_squares(a, b, n)
        a, b = dynamic_power(a, b, m - n)
        return multiply(x, y, a, b)


def digits_sequence(n):
    a, b = dynamic_power(mpz(1), mpz(0), mpz(n))
    return a

