import abc

from src.domain import models


class PaymentGatewayPort(abc.ABC):
    """Port: contract that every payment gateway adapter must satisfy."""

    @abc.abstractmethod
    def charge(self, amount: float, currency: str, card_token: str) -> models.PaymentResult:
        """Charge *amount* to the card identified by *card_token*."""
        ...

    @abc.abstractmethod
    def refund(self, transaction_id: str, amount: float) -> models.PaymentResult:
        """Refund *amount* for the given *transaction_id*."""
        ...
