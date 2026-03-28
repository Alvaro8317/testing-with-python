import pytest
from src import car_shopping_2


@pytest.mark.raise_exception
def test_should_raise_value_error_because_price_is_negative() -> None:
    car = car_shopping_2.CarShopping()
    with pytest.raises(car_shopping_2.InvalidFieldException):
        car.add("laptop", -110)


@pytest.mark.raise_exception
def test_should_raise_value_error_because_price_is_negative_2() -> None:
    car = car_shopping_2.CarShopping()
    with pytest.raises(car_shopping_2.InvalidFieldException, match="than 0"):
        car.add("laptop", -110)


@pytest.mark.raise_exception
def test_should_raise_value_error_because_price_is_negative_3() -> None:
    car = car_shopping_2.CarShopping()
    with pytest.raises(car_shopping_2.InvalidFieldException, match="than 0") as excinfo:
        car.add("laptop", -110)
    assert excinfo.type is car_shopping_2.PriceCanNotBeLessThanZeroException


@pytest.mark.raise_exception
def test_should_raise_value_error_because_price_is_negative_4() -> None:
    car = car_shopping_2.CarShopping()
    pytest.raises(car_shopping_2.PriceCanNotBeLessThanZeroException, car.add, "laptop", -110)


@pytest.mark.raise_exception
@pytest.mark.parametrize(
    "product, price, message_error, expected_exception",
    [
        pytest.param("laptop", -100, "than 0", car_shopping_2.PriceCanNotBeLessThanZeroException),
        pytest.param("", 100, "empty", car_shopping_2.InvalidFieldException),
    ],
)
def test_should_parametrize_several_use_cases(
    product: str, price: int | float, message_error: str, expected_exception: type[Exception]
) -> None:
    car = car_shopping_2.CarShopping()
    with pytest.raises(expected_exception, match=message_error):
        car.add(product=product, price=price)
