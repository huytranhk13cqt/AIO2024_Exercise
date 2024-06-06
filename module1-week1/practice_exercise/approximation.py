import math


def factorial(n):
    if n < 0:
        return math.nan
    elif n == 0:
        return 1
    return n * factorial(n - 1)


def sin_approximation(x, terms):
    sin_x = sum(((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(terms))
    return sin_x


def cos_approximation(x, terms):
    cos_x = sum(((-1) ** i) * (x ** (2 * i)) / factorial(2 * i) for i in range(terms))
    return cos_x


def sinh_approximation(x, terms):
    sinh_x = sum((x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(terms))
    return sinh_x


def cosh_approximation(x, terms):
    cosh_x = sum((x ** (2 * i)) / factorial(2 * i) for i in range(terms))
    return cosh_x
