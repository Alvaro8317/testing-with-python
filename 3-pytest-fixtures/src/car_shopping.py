import decimal


class CarShopping:
    def __init__(self) -> None:
        self.items = []

    def add(self, product: str, price: int | float | decimal.Decimal) -> None:
        self.items.append({"product": product, "price": price})

    def total(self) -> int | float | decimal.Decimal:
        return sum(item["price"] for item in self.items)

    def empty(self) -> None:
        self.items.clear()
