# Calculator.py 

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return a ** b


def sqrt(a):
    if a < 0:
        raise ValueError("Square root of negative number is not real.")
    return math.sqrt(a)


def factorial(n):
    if n < 0:
        raise ValueError(
            "Factorial is only defined for non-negative integers."
        )
    return math.factorial(n)


def log(a, base=10):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers.")
    return math.log(a, base)
