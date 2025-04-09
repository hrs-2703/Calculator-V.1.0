# tests/test_calculator.py

import pytest
import calculator


def test_add():
    assert calculator.add(2, 3) == 5


def test_subtract():
    assert calculator.subtract(5, 2) == 3


def test_multiply():
    assert calculator.multiply(3, 4) == 12


def test_divide():
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(4, 0)


def test_power():
    assert calculator.power(2, 3) == 8


def test_sqrt():
    assert calculator.sqrt(9) == 3


def test_sqrt_negative():
    with pytest.raises(ValueError):
        calculator.sqrt(-4)


def test_factorial():
    assert calculator.factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError):
        calculator.factorial(-1)


def test_log():
    assert round(calculator.log(100, 10), 2) == 2


def test_log_invalid():
    with pytest.raises(ValueError):
        calculator.log(-10)
