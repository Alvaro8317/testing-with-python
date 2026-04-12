from src import number_utils


def test_should_validate_if_a_year_is_leap() -> None:
    assert number_utils.is_leap_year(2000)


def test_should_convert_celsius() -> None:
    assert number_utils.celsius_to_fahrenheit(0) == 32.0
