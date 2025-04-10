"""Calculatr module providing various mathematical operations."""

import math


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division of two numbers.Error on div by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


def sqrt(a):
    """Return the square root of a number. Error for neg input."""
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(a)


def factorial(n):
    """Return the factorial of a non-neg integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-neg integers.")
    return math.factorial(n)


def log(a, base=10):
    """Return the log of a number with base.Error for non-pos input."""
    if a <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    return math.log(a, base)
