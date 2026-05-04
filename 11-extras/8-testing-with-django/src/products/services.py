from decimal import Decimal
from typing import TypedDict

from products import models


class CartItem(TypedDict):
    price: Decimal
    quantity: int


def calculate_discount(price: Decimal, discount_percentage: int | float) -> Decimal:
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    discount = price * Decimal(str(discount_percentage)) / Decimal("100")
    return price - discount


def apply_tax(price: Decimal, tax_rate: int | float | Decimal) -> Decimal:
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    return price * (Decimal("1") + Decimal(str(tax_rate)))


def calculate_total(items: list[CartItem]) -> Decimal:
    return sum(
        (item["price"] * item["quantity"] for item in items),
        Decimal("0"),
    )


def filter_available_products(products: list[models.Product]) -> list[models.Product]:
    return [p for p in products if p.is_available()]
