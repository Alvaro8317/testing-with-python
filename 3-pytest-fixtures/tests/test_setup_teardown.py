from collections.abc import Generator

import pytest


class CarShoppingSetup:
    _log = []

    def __init__(self) -> None:
        self.items = []

    def add(self, product: str, price: int) -> None:
        self.items.append({"product": product, "price": price})
        CarShoppingSetup._log.append(f"Added {product}")

    def total(self) -> int:
        return sum(item["price"] for item in self.items)

    def empty(self) -> None:
        self.items = []


@pytest.fixture
def fxt_car() -> Generator[CarShoppingSetup]:
    print("\n→ Creando carrito")
    cart = CarShoppingSetup()

    yield cart

    print("\n→ Limpiando log compartido")
    CarShoppingSetup._log.clear()


@pytest.mark.unittest
def test_should_car_1(fxt_car: CarShoppingSetup) -> None:
    fxt_car.add(product="Another product", price=100)
    assert fxt_car.total() == 100
    print(fxt_car._log)


@pytest.mark.unittest
def test_should_car_2(fxt_car: CarShoppingSetup) -> None:
    fxt_car.add(product="Another product 2", price=100)
    assert fxt_car.total() == 100
    print(fxt_car._log)
