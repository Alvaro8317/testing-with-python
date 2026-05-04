from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class Customer:
    id: int
    name: str
    email: str
    age: int
    is_premium: bool = False

    def can_place_order(self) -> bool:
        return bool(self.name and self.email)


@dataclass
class Product:
    id: int
    name: str
    price: Decimal
    stock: int

    def is_available(self) -> bool:
        return self.stock > 0


@dataclass
class OrderItem:
    product: Product
    quantity: int

    def subtotal(self) -> Decimal:
        return self.product.price * self.quantity


@dataclass
class Order:
    id: int
    customer: Customer
    items: list[OrderItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.PENDING

    def total(self) -> Decimal:
        return sum(item.subtotal() for item in self.items)  # type: ignore

    def item_count(self) -> int:
        return sum(item.quantity for item in self.items)

    def confirm(self) -> None:
        if not self.items:
            raise ValueError("Cannot confirm an order with no items")
        self.status = OrderStatus.CONFIRMED

    def cancel(self) -> None:
        if self.status == OrderStatus.SHIPPED:
            raise ValueError("Cannot cancel a shipped order")
        self.status = OrderStatus.CANCELLED

    def apply_premium_discount(self) -> Decimal:
        if not self.customer.is_premium:
            return self.total()
        return self.total() * Decimal("0.9")
