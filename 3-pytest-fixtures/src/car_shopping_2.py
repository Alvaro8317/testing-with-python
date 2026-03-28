import decimal


class InvalidFieldException(Exception): ...


class PriceCanNotBeLessThanZeroException(InvalidFieldException): ...


class CarShopping:
    def __init__(self) -> None:
        self.items = []

    def add(self, product: str, price: int | float | decimal.Decimal) -> None:
        if price < 0:
            raise PriceCanNotBeLessThanZeroException("The price can not be less than 0")
        if not product or not product.strip():
            raise InvalidFieldException("The name of the product can not be empty")
        self.items.append({"product": product, "price": price})

    def total(self) -> int | float | decimal.Decimal:
        return sum(item["price"] for item in self.items)

    def empty(self) -> None:
        self.items.clear()
