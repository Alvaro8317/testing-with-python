class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self) -> str:
        return f"Product({self.name!r}, price={self.price}, stock={self.stock})"


class ShoppingCart:
    def __init__(self) -> None:
        self._items: dict[Product, int] = {}

    def add(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        if product.stock < quantity:
            raise ValueError(f"Stock insuficiente para '{product.name}'")
        self._items[product] = self._items.get(product, 0) + quantity

    def remove(self, product: Product) -> None:
        if product not in self._items:
            raise KeyError(f"'{product.name}' no está en el carrito")
        del self._items[product]

    def total(self) -> float:
        return sum(p.price * qty for p, qty in self._items.items())

    def item_count(self) -> int:
        return sum(self._items.values())

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def contains(self, product: Product) -> bool:
        return product in self._items

    def clear(self) -> None:
        self._items.clear()
