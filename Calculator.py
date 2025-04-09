"""Calculator module providing various mathematical operations."""

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
    """Return the division of two numbers. Raise error on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


def sqrt(a):
    """Return the square root of a number. Raise error for negative input."""
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(a)


def factorial(n):
    """Return the factorial of a non-negative integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(n)


def log(a, base=10):
    """Return the logarithm of a number with a specified base. Raise error for non-positive input."""
    if a <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    return math.log(a, base)
