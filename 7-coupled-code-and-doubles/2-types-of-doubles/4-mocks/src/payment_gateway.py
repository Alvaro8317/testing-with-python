class PaymentGateway:
    """Pasarela de pago real (nunca llamar en tests — cobra dinero real)."""

    def charge(self, card_token: str, amount: float, currency: str) -> dict:
        raise NotImplementedError("Procesa pago real")

    def refund(self, transaction_id: str, amount: float) -> dict:
        raise NotImplementedError("Procesa reembolso real")
