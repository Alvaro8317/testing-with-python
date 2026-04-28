# Un Dummy es un objeto que se pasa como argumento pero nunca se usa realmente.
# Su único propósito es satisfacer la firma del método cuando el parámetro
# no es relevante para el comportamiento que estamos probando.

import requests


class Logger:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


class Order:
    def __init__(self, product: str, quantity: int):
        self.product = product
        self.quantity = quantity


CACHE_ORDERS = {1: Order(product="A nice product", quantity=210)}


class OrderService:
    def __init__(self, logger: Logger) -> None:
        # El logger es una dependencia real, pero en ciertos tests no importa
        self._logger = logger

    def calculate_total(self, order: Order, price_per_unit: float) -> float:
        # El logger existe pero no afecta el cálculo
        self._logger.log(f"Calculando total para {order.product}")
        return order.quantity * price_per_unit

    def get_order(self, id_order: int, http_response: requests.Response) -> Order:
        order = CACHE_ORDERS.get(id_order)
        if order:
            return order
        # Código que solo se necesitará si no lo encuentra en caché
        return http_response.json().get(id_order)
