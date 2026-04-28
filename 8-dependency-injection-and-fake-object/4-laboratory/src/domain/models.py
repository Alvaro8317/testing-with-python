from dataclasses import dataclass


@dataclass
class Order:
    order_id: str
    amount: float
    currency: str
    card_token: str


@dataclass
class PaymentResult:
    success: bool
    transaction_id: str
    message: str
