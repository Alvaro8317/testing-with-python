import pytest
from src import car_shopping


@pytest.mark.integration
def test_should_add_and_empty_items_car_shopping(
    fxt_car_shared_conftest: car_shopping.CarShopping,
) -> None:
    fxt_car_shared_conftest.add(product="fake product", price=100)
    assert fxt_car_shared_conftest.total() == 100
    fxt_car_shared_conftest.empty()
    assert fxt_car_shared_conftest.total() == 0
