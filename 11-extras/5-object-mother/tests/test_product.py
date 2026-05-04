from decimal import Decimal
from tests.mothers import ProductMother


def test_should_confirm_product_is_available_when_stock_is_positive():
    product = ProductMother.default()

    assert product.is_available() is True


def test_should_confirm_product_is_unavailable_when_stock_is_zero():
    product = ProductMother.out_of_stock()

    assert product.is_available() is False


def test_should_create_cheap_product_with_low_price():
    product = ProductMother.cheap()

    assert product.price < Decimal("50.00")


def test_should_create_product_with_custom_price():
    product = ProductMother.create(price=Decimal("249.99"))

    assert product.price == Decimal("249.99")


def test_should_create_product_with_custom_stock():
    product = ProductMother.create(stock=5)

    assert product.stock == 5
