from src.domain import models, payment_gateway


class StripePaymentAdapter(payment_gateway.PaymentGatewayPort):
    """Real Stripe adapter — requires a live API key and network access.

    Cannot be used in unit tests: instantiating it with a valid key and
    hitting the Stripe sandbox costs money and introduces network flakiness.
    Use FakePaymentGateway in tests instead.
    """

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def charge(self, amount: float, currency: str, card_token: str) -> models.PaymentResult:
        # Real implementation would call: stripe.PaymentIntent.create(...)
        raise NotImplementedError(
            "StripePaymentAdapter requires a live Stripe connection. "
            "Use FakePaymentGateway in unit tests."
        )

    def refund(self, transaction_id: str, amount: float) -> models.PaymentResult:
        # Real implementation would call: stripe.Refund.create(...)
        raise NotImplementedError(
            "StripePaymentAdapter requires a live Stripe connection. "
            "Use FakePaymentGateway in unit tests."
        )
