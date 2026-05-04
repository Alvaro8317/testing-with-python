from decimal import Decimal

import pytest
from products import models, services


def test_should_calculate_discount_correctly() -> None:
    price = Decimal("100.00")
    result = services.calculate_discount(price, 20)
    assert result == Decimal("80.00")


def test_should_return_original_price_when_discount_is_zero() -> None:
    price = Decimal("100.00")
    result = services.calculate_discount(price, 0)
    assert result == price


def test_should_apply_full_discount_when_percentage_is_100() -> None:
    price = Decimal("100.00")
    result = services.calculate_discount(price, 100)
    assert result == Decimal("0.00")


def test_should_raise_error_when_discount_exceeds_100() -> None:
    with pytest.raises(ValueError):
        services.calculate_discount(Decimal("100.00"), 150)


def test_should_raise_error_when_discount_is_negative() -> None:
    with pytest.raises(ValueError):
        services.calculate_discount(Decimal("100.00"), -10)


def test_should_apply_tax_correctly() -> None:
    price = Decimal("100.00")
    result = services.apply_tax(price, Decimal("0.19"))
    assert result == Decimal("119.00")


def test_should_not_modify_price_when_tax_rate_is_zero() -> None:
    price = Decimal("100.00")
    result = services.apply_tax(price, 0)
    assert result == price


def test_should_raise_error_when_tax_rate_is_negative() -> None:
    with pytest.raises(ValueError):
        services.apply_tax(Decimal("100.00"), -0.05)


def test_should_calculate_total_for_multiple_items() -> None:
    items: list[services.CartItem] = [
        {"price": Decimal("10.00"), "quantity": 2},
        {"price": Decimal("5.00"), "quantity": 3},
    ]
    result = services.calculate_total(items)
    assert result == Decimal("35.00")


def test_should_return_zero_for_empty_cart() -> None:
    result = services.calculate_total([])
    assert result == Decimal("0")


def test_should_calculate_total_for_single_item() -> None:
    items: list[services.CartItem] = [{"price": Decimal("25.50"), "quantity": 4}]
    result = services.calculate_total(items)
    assert result == Decimal("102.00")


def test_should_filter_available_products(
    product: models.Product, out_of_stock_product: models.Product, inactive_product: models.Product
) -> None:
    all_products: list[models.Product] = [product, out_of_stock_product, inactive_product]
    result = services.filter_available_products(all_products)
    assert len(result) == 1
    assert result[0].name == "Test Product"


def test_should_return_empty_list_when_no_products_are_available(
    out_of_stock_product: models.Product, inactive_product: models.Product
) -> None:
    all_products: list[models.Product] = [out_of_stock_product, inactive_product]
    result = services.filter_available_products(all_products)
    assert result == []
