from src import calculadora


def test_divide_two_numbers() -> None:
    result = calculadora.divide(10, 2)
    assert result == 5


def test_divide_two_numbers_2() -> None:
    result = calculadora.divide(20, 2)
    assert result == 10


def test_divide_two_numbers_3() -> None:
    result = calculadora.divide(100, 2)
    assert result == 50
