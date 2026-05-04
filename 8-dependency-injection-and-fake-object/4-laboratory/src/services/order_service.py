from src.domain import models, payment_gateway


class OrderService:
    def __init__(self, payment_gateway: payment_gateway.PaymentGatewayPort) -> None:
        self._gateway = payment_gateway

    def process_order(self, order: models.Order) -> models.PaymentResult:
        if order.amount <= 0:
            raise ValueError("Order amount must be positive")
        return self._gateway.charge(order.amount, order.currency, order.card_token)

    def cancel_order(self, transaction_id: str, amount: float) -> models.PaymentResult:
        if amount <= 0:
            raise ValueError("Refund amount must be positive")
        return self._gateway.refund(transaction_id, amount)
