from src import pricing


def test_should_calculate_price_without_discount() -> None:
    assert pricing.calculate_final_price(price=100.0, discount_percent=0) == 100.0


def test_should_calculate_price_with_ten_percent_discount() -> None:
    assert pricing.calculate_final_price(price=100.0, discount_percent=10) == 90.0
