import uuid

from src.domain import models, payment_gateway


class FakePaymentGateway(payment_gateway.PaymentGatewayPort):
    """Fake implementation of PaymentGateway for use in unit tests.

    A *fake* is a simplified but working implementation that is not suitable
    for production.  Unlike a mock (which only records calls), a fake has
    real — though minimal — logic.

    ─────────────────────────────────────────────────────────────────────────
    YOUR TASKS
    ─────────────────────────────────────────────────────────────────────────
    1. Add the attributes you need to track state (e.g. charged_payments,
       should_fail).  Initialize them in __init__.

    2. Implement `charge` so that:
       a. It records every call in self.charged_payments (list of dicts with
          keys "amount", "currency" and "card_token").
       b. When self.should_fail is True it returns a failure PaymentResult.
       c. Otherwise it returns a successful PaymentResult with a deterministic
          transaction_id such as "fake-txn-1", "fake-txn-2", … (use a counter) uuid.

    3. Implement `refund` so that it always returns a successful PaymentResult.

    Hints
    ─────
    • PaymentResult(success, transaction_id, message) is a plain dataclass.
    • You do NOT need to import anything beyond what is already imported here.
    ─────────────────────────────────────────────────────────────────────────
    """

    def __init__(self) -> None:
        # TODO: initialize your state here
        # Example attributes you may want:
        self.charged_payments: list[dict] = []
        #   self.should_fail: bool = False
        #   self._charge_counter: int = 0
        pass

    def charge(self, amount: float, currency: str, card_token: str) -> models.PaymentResult:
        transaction_id = str(uuid.uuid4())
        self.charged_payments.append(
            {
                "amount": amount,
                "currency": currency,
                "card_token": card_token,
                "transaction_id": transaction_id,
            }
        )
        return models.PaymentResult(
            success=True, transaction_id=transaction_id, message="Charge successful"
        )

    def refund(self, transaction_id: str, amount: float) -> models.PaymentResult:
        payment = next(
            (txn for txn in self.charged_payments if txn["transaction_id"] == transaction_id), None
        )
        if not payment:
            return models.PaymentResult(
                success=False, transaction_id=transaction_id, message="Transaction not found"
            )
        if amount > payment["amount"]:
            return models.PaymentResult(
                success=False,
                transaction_id=transaction_id,
                message="Refund amount exceeds original charge",
            )
        return models.PaymentResult(
            success=True, transaction_id=transaction_id, message="Refund successful"
        )
