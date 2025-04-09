# test_calculator.py

import pytest
import calculator

def test_add(): assert calculator.add(3, 2) == 5
def test_subtract(): assert calculator.subtract(5, 3) == 2
def test_multiply(): assert calculator.multiply(4, 2) == 8
def test_divide(): assert calculator.divide(10, 2) == 5
def test_divide_by_zero(): with pytest.raises(ValueError): calculator.divide(4, 0)
def test_power(): assert calculator.power(2, 3) == 8
def test_mod(): assert calculator.mod(10, 3) == 1
def test_sqrt(): assert calculator.sqrt(25) == 5
def test_sqrt_negative(): with pytest.raises(ValueError): calculator.sqrt(-9)
def test_factorial(): assert calculator.factorial(5) == 120
def test_factorial_negative(): with pytest.raises(ValueError): calculator.factorial(-2)
def test_factorial_float(): with pytest.raises(ValueError): calculator.factorial(4.5)
def test_log_base10(): assert round(calculator.log(100), 2) == 2.00
def test_log_custom_base(): assert round(calculator.log(8, 2), 2) == 3.00
def test_log_negative(): with pytest.raises(ValueError): calculator.log(-1)
