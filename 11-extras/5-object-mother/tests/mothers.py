from decimal import Decimal

from src.models import Customer, Order, OrderItem, OrderStatus, Product


class CustomerMother:
    @staticmethod
    def default() -> Customer:
        return Customer(
            id=1, name="John Doe", email="john.doe@example.com", is_premium=False, age=28
        )

    @staticmethod
    def create(
        id: int = 1,
        name: str = "John Doe",
        age: int = 28,
        email: str = "john.doe@example.com",
        is_premium: bool = False,
    ) -> Customer:
        return Customer(id=id, name=name, email=email, is_premium=is_premium, age=age)

    @staticmethod
    def premium() -> Customer:
        return CustomerMother.create(
            id=2, name="Jane Smith", email="jane.smith@example.com", is_premium=True
        )

    @staticmethod
    def without_email() -> Customer:
        return CustomerMother.create(email="")


class ProductMother:
    @staticmethod
    def default() -> Product:
        return ProductMother.create()

    @staticmethod
    def create(
        id: int = 1,
        name: str = "Laptop",
        price: Decimal = Decimal("999.99"),
        stock: int = 10,
    ) -> Product:
        return Product(id=id, name=name, price=price, stock=stock)

    @staticmethod
    def out_of_stock() -> Product:
        return ProductMother.create(id=99, name="Sold Out Item", stock=0)

    @staticmethod
    def cheap() -> Product:
        return ProductMother.create(id=3, name="USB Cable", price=Decimal("9.99"), stock=100)


class OrderMother:
    @staticmethod
    def default() -> Order:
        customer = CustomerMother.default()
        product = ProductMother.default()
        return Order(
            id=1,
            customer=customer,
            items=[OrderItem(product=product, quantity=1)],
            status=OrderStatus.PENDING,
        )

    @staticmethod
    def create(
        id: int = 1,
        customer: Customer | None = None,
        items: list | None = None,
        status: OrderStatus = OrderStatus.PENDING,
    ) -> Order:
        return Order(
            id=id,
            customer=customer or CustomerMother.default(),
            items=items or [OrderItem(product=ProductMother.default(), quantity=1)],
            status=status,
        )

    @staticmethod
    def empty() -> Order:
        return Order(id=2, customer=CustomerMother.default(), items=[], status=OrderStatus.PENDING)

    @staticmethod
    def confirmed() -> Order:
        return OrderMother.create(id=3, status=OrderStatus.CONFIRMED)

    @staticmethod
    def shipped() -> Order:
        return OrderMother.create(id=4, status=OrderStatus.SHIPPED)

    @staticmethod
    def for_premium_customer() -> Order:
        return OrderMother.create(id=5, customer=CustomerMother.premium())
