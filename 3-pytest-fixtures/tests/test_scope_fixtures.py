import os

import pytest


class CarShopping:
    items: int = 0

    def add_quantity_items(self, quantity: int) -> None:
        self.items += quantity


@pytest.fixture(scope="module")
def fxt_car_shopping() -> CarShopping:
    return CarShopping()


@pytest.mark.skip(reason="Is not stable this code")
def test_should_have_10_items(fxt_car_shopping: CarShopping) -> None:
    print("Items al iniciar: ", fxt_car_shopping.items)
    fxt_car_shopping.add_quantity_items(10)
    assert fxt_car_shopping.items == 10


@pytest.mark.skip(reason="Is not stable this code")
def test_should_have_50_items(fxt_car_shopping: CarShopping) -> None:
    print("Items al iniciar: ", fxt_car_shopping.items)
    fxt_car_shopping.add_quantity_items(50)
    assert fxt_car_shopping.items == 50


@pytest.mark.skip(reason="Is not stable this code")
def test_should_have_100_items(fxt_car_shopping: CarShopping) -> None:
    print("Items al iniciar: ", fxt_car_shopping.items)
    fxt_car_shopping.add_quantity_items(100)
    assert fxt_car_shopping.items == 100


@pytest.mark.skipif(
    condition=os.getenv("SHOULD_RUN", False), reason="It only for education purpose"
)
def test_should_have_200_items(fxt_car_shopping: CarShopping) -> None:
    fxt_car_shopping.add_quantity_items(100)
    assert fxt_car_shopping.items == 100
