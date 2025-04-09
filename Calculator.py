# calculator.py is modified

import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b): return a ** b
def mod(a, b): return a % b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def factorial(n):
    if n < 0 or not float(n).is_integer():
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(int(n))

def log(a, base=10):
    if a <= 0:
        raise ValueError("Logarithm undefined for zero or negative numbers.")
    return math.log(a, base)
