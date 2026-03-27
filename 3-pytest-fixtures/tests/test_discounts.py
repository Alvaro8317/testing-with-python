import pydantic
import pytest
from src import discounts


@pytest.mark.discounts
def test_should_calculate_price_without_discount() -> None:
    product = discounts.ProductPurchase(price=100.0, quantity=1, percentaje_discount=0)
    assert discounts.calculate_final_price(product=product) == 100.0


@pytest.mark.discounts
def test_should_calculate_price_with_partial_discount() -> None:
    product = discounts.ProductPurchase(price=100.0, quantity=1, percentaje_discount=10)
    assert discounts.calculate_final_price(product=product) == 90.0


@pytest.mark.discounts
def test_should_calculate_price_with_multiple_units() -> None:
    product = discounts.ProductPurchase(price=50.0, quantity=3, percentaje_discount=0)
    assert discounts.calculate_final_price(product=product) == 150.0


@pytest.mark.discounts  # Justo en el limite inferior
def test_should_calculate_price_with_zero_percent() -> None:
    product = discounts.ProductPurchase(price=50.0, quantity=1, percentaje_discount=0)
    assert discounts.calculate_final_price(product=product) == 50.0


@pytest.mark.discounts  # Justo en el limite superior
def test_should_calculate_price_with_one_hundred_percent() -> None:
    product = discounts.ProductPurchase(price=50.0, quantity=1, percentaje_discount=100)
    assert discounts.calculate_final_price(product=product) == 0.0


@pytest.mark.discounts  # Justo por debajo del limite inferior
def test_should_calculate_price_with_negative_discount() -> None:
    with pytest.raises(pydantic.ValidationError):
        discounts.ProductPurchase(price=50.0, quantity=1, percentaje_discount=-1)


@pytest.mark.discounts  # Justo por encima del limite superior
def test_should_calculate_price_with_a_discount_more_than_one_hundred() -> None:
    with pytest.raises(pydantic.ValidationError):
        discounts.ProductPurchase(price=50.0, quantity=1, percentaje_discount=101)
