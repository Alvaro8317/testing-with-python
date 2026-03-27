import pytest
from src import car_shopping


@pytest.fixture
def fxt_car_shopping() -> car_shopping.CarShopping:
    return car_shopping.CarShopping()


@pytest.mark.critical
def test_should_add_item_and_show_the_total(fxt_car_shopping: car_shopping.CarShopping) -> None:
    fxt_car_shopping.add(product="Laptop", price=1000)
    assert fxt_car_shopping.total() == 1000


@pytest.mark.critical
def test_should_add_several_items_and_show_the_total(
    fxt_car_shopping: car_shopping.CarShopping,
) -> None:
    fxt_car_shopping.add(product="Laptop", price=1000)
    fxt_car_shopping.add(product="Mouse", price=50)
    assert fxt_car_shopping.total() == 1050


@pytest.mark.critical
def test_should_empty_the_car(fxt_car_shopping: car_shopping.CarShopping) -> None:
    fxt_car_shopping.add(product="Laptop", price=1000)
    fxt_car_shopping.add(product="Mouse", price=50)
    assert fxt_car_shopping.total() == 1050
    fxt_car_shopping.empty()
    assert fxt_car_shopping.total() == 0
