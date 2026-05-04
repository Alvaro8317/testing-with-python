import pytest
from decimal import Decimal
from src.models import OrderStatus
from tests.mothers import CustomerMother, OrderMother, ProductMother
from src.models import OrderItem


def test_should_calculate_correct_total_for_default_order():
    order = OrderMother.default()

    assert order.total() == Decimal("999.99")


def test_should_confirm_order_when_it_has_items():
    order = OrderMother.default()

    order.confirm()

    assert order.status == OrderStatus.CONFIRMED


def test_should_raise_error_when_confirming_empty_order():
    order = OrderMother.empty()

    with pytest.raises(ValueError, match="no items"):
        order.confirm()


def test_should_cancel_pending_order():
    order = OrderMother.default()

    order.cancel()

    assert order.status == OrderStatus.CANCELLED


def test_should_cancel_confirmed_order():
    order = OrderMother.confirmed()

    order.cancel()

    assert order.status == OrderStatus.CANCELLED


def test_should_raise_error_when_cancelling_shipped_order():
    order = OrderMother.shipped()

    with pytest.raises(ValueError, match="shipped"):
        order.cancel()


def test_should_apply_10_percent_discount_for_premium_customer():
    order = OrderMother.for_premium_customer()
    expected = order.total() * Decimal("0.9")

    discounted = order.apply_premium_discount()

    assert discounted == expected


def test_should_not_apply_discount_for_regular_customer():
    order = OrderMother.default()

    discounted = order.apply_premium_discount()

    assert discounted == order.total()


def test_should_count_total_items_in_order():
    cheap_product = ProductMother.cheap()
    expensive_product = ProductMother.default()
    order = OrderMother.create(
        items=[
            OrderItem(product=cheap_product, quantity=3),
            OrderItem(product=expensive_product, quantity=2),
        ]
    )

    assert order.item_count() == 5


def test_should_create_order_with_custom_customer():
    vip_customer = CustomerMother.create(id=99, name="VIP Customer", is_premium=True)
    order = OrderMother.create(customer=vip_customer)

    assert order.customer.name == "VIP Customer"
    assert order.customer.is_premium is True
