import decimal


class CarShopping:
    def __init__(self) -> None:
        self.items = []

    def add(self, producto: str, precio: int | float | decimal.Decimal) -> None:
        self.items.append({"producto": producto, "precio": precio})

    def total(self) -> int:
        return sum(item["precio"] for item in self.items)

    def empty(self) -> None:
        self.items.clear()
