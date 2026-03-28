import pytest
from src import car_shopping


@pytest.fixture
def fxt_car_shopping_indirect(request: pytest.FixtureRequest) -> car_shopping.CarShopping:
    product_name, price_product = request.param
    car_to_return = car_shopping.CarShopping()
    car_to_return.add(product=product_name, price=price_product)
    return car_to_return


@pytest.mark.parametrize(
    "fxt_car_shopping_indirect",
    [("laptop", 1000), ("mouse", 50), ("keyboard", 150), ("PS5", 550), ("PCGamer", 3000)],
    indirect=True,
)
def test_should_create_car_shopping(fxt_car_shopping_indirect: car_shopping.CarShopping) -> None:
    assert fxt_car_shopping_indirect.total() >= 0
