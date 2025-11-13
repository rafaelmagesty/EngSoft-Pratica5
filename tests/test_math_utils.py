import math
import pytest

from src.math_utils import (
    factorial,
    fibonacci,
    is_palindrome,
    normalize,
    sum_even_numbers,
)


def test_factorial_positive():
    assert factorial(5) == math.factorial(5)


def test_factorial_negative_raises_value_error():
    with pytest.raises(ValueError):
        factorial(-1)


def test_fibonacci_value():
    assert fibonacci(10) == 55


def test_is_palindrome_various_cases():
    assert is_palindrome("Ame a ema")
    assert not is_palindrome("Python")


def test_sum_even_numbers_filters_correctly():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12


def test_sum_even_numbers_invalid_type_raises():
    with pytest.raises(TypeError):
        sum_even_numbers([1, 2, "3"])  # type: ignore[list-item]


def test_normalize_returns_expected_values():
    resultado = normalize([10.0, 15.0, 20.0])
    assert resultado == [0.0, 0.5, 1.0]


def test_normalize_single_value_raises_error():
    with pytest.raises(ValueError):
        normalize([2, 2, 2])




