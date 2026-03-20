from src import calculadora


class TestDivide:
    def test_divide_two_numbers(self) -> None:
        result = calculadora.divide(10, 2)
        assert result == 5

    def test_divide_two_numbers_with_decimals(self) -> None:
        result = calculadora.divide(7, 2)
        assert result == 3.5
