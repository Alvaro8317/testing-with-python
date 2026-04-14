import dataclasses


@dataclasses.dataclass
class Order:
    order_name: str
    order_id: str


def get_order() -> Order:
    raise ConnectionError()
