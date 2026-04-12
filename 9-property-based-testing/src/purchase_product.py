import pydantic


class PurchaseProduct(pydantic.BaseModel):
    price: float
    quantity: int
    percetaje_discount: float


class ConnectionDB:
    def __init__(self, connection_string: str) -> None:
        self.connection_string: str


def calculate_final_price(product: PurchaseProduct) -> float:
    discount = product.price * (product.percetaje_discount / 100)
    return round((product.price - discount) * product.quantity, 2)
