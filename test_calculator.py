"""Unit tests for the calculator module."""

import pytest
from calculator import calculator


def test_add():
    """Test addition of two numbers."""
    assert calculator.add(2, 3) == 5


def test_subtract():
    """Test subtraction of two numbers."""
    assert calculator.subtract(5, 2) == 3


def test_multiply():
    """Test multiplication of two numbers."""
    assert calculator.multiply(3, 4) == 12


def test_divide():
    """Test division of two numbers."""
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero():
    """Test division by zero raises error."""
    with pytest.raises(ValueError):
        calculator.divide(4, 0)


def test_power():
    """Test exponentiation."""
    assert calculator.power(2, 3) == 8


def test_sqrt():
    """Test square root."""
    assert calculator.sqrt(9) == 3


def test_sqrt_negative():
    """Test square root of a negative number raises error."""
    with pytest.raises(ValueError):
        calculator.sqrt(-4)


def test_factorial():
    """Test factorial."""
    assert calculator.factorial(5) == 120


def test_factorial_negative():
    """Test factorial of negative number raises error."""
    with pytest.raises(ValueError):
        calculator.factorial(-1)


def test_log():
    """Test base-10 logarithm."""
    assert round(calculator.log(100, 10), 2) == 2


def test_log_invalid():
    """Test log of negative number raises error."""
    with pytest.raises(ValueError):
        calculator.log(-10)
