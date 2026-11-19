from src.calc import add, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_zero_and_negative():
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
