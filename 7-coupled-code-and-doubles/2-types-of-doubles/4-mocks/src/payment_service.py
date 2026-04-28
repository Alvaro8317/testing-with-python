# Un Mock es un doble que tiene expectativas preconfiguradas sobre cómo debe ser usado.
# El mock verifica automáticamente que se llamaron los métodos correctos con los
# argumentos correctos. Si las expectativas no se cumplen, el test falla.
from src import payment_gateway


class PaymentService:
    def __init__(self) -> None:
        self._gateway = payment_gateway.PaymentGateway()

    def process_order_payment(self, card_token: str, amount: float) -> dict:
        if amount <= 0:
            raise ValueError("El monto debe ser mayor a cero")

        result = self._gateway.charge(
            card_token=card_token,
            amount=amount,
            currency="USD",
        )
        return result

    def cancel_order(self, transaction_id: str, amount: float) -> dict:
        return self._gateway.refund(
            transaction_id=transaction_id,
            amount=amount,
        )
