# Write pytest for  calc.py
import pytest
from calc import add, subtract, multiply, divide, mod


def test_add():
    assert add(2, 3) == 5
    assert add(7, -7) == 0


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(6, 3) == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)


def test_mod():
    assert mod(5, 3) == 2
    assert mod(10, 5) == 0


def test_mod_by_zero():
    with pytest.raises(ZeroDivisionError):
        mod(6, 0)
