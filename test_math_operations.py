import pytest
from math_operations import add_numbers

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300)
])
def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected