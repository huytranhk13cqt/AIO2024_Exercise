import math


def factorial(n):
    # Calculate factorial, return NaN if n is negative
    if n < 0:
        return math.nan
    elif n == 0:
        return 1
    return n * factorial(n - 1)


def sin_approximation(x, terms):
    # Approximate sine of x using Taylor series
    return sum(((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(terms))


def cos_approximation(x, terms):
    # Approximate cosine of x using Taylor series
    return sum(((-1) ** i) * (x ** (2 * i)) / factorial(2 * i) for i in range(terms))


def sinh_approximation(x, terms):
    # Approximate hyperbolic sine of x using Taylor series
    return sum((x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(terms))


def cosh_approximation(x, terms):
    # Approximate hyperbolic cosine of x using Taylor series
    return sum((x ** (2 * i)) / factorial(2 * i) for i in range(terms))
