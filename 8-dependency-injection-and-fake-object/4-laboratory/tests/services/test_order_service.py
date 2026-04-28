"""Unit tests for OrderService.

─────────────────────────────────────────────────────────────────────────────
YOUR TASKS
─────────────────────────────────────────────────────────────────────────────
1. Finish implementing FakePaymentGateway in tests/fakes/fake_payment_gateway.py.
2. Import it below (replace the TODO comment).
3. Complete every test method so that each one has at least one assertion.
4. Run the suite with:  pytest tests/ -v

Rules
─────
• Use FakePaymentGateway — never StripePaymentAdapter — in these tests.
• Do not patch or monkeypatch anything.  Inject the fake through __init__.
─────────────────────────────────────────────────────────────────────────────
"""

import uuid

import pytest
from src.domain import models
from src.services import order_service

from tests.fakes import fake_payment_gateway


@pytest.mark.payments
class TestProcessOrder:
    def test_successful_charge_returns_success_result(self) -> None:
        fake_adapter = fake_payment_gateway.FakePaymentGateway()
        order_srv = order_service.OrderService(payment_gateway=fake_adapter)
        order = models.Order(
            order_id=str(uuid.uuid4()), amount=100.0, currency="USD", card_token="fake-card-token"
        )
        result = order_srv.process_order(order=order)
        assert result.success is True

    def test_charge_is_recorded_in_fake(self) -> None:
        # TODO: after calling process_order, inspect fake.charged_payments
        # TODO: assert that exactly one payment was recorded
        # TODO: assert the recorded amount matches the order amount
        pass

    def test_currency_is_forwarded_to_gateway(self) -> None:
        # TODO: create an Order with currency="EUR"
        # TODO: assert the recorded payment has currency "EUR"
        pass

    def test_process_order_raises_when_amount_is_zero(self) -> None:
        # TODO: create an Order with amount=0
        # TODO: use pytest.raises to assert that process_order raises ValueError
        pass

    def test_process_order_raises_when_amount_is_negative(self) -> None:
        # TODO: create an Order with a negative amount
        # TODO: use pytest.raises to assert that process_order raises ValueError
        pass

    def test_gateway_failure_is_returned_to_caller(self) -> None:
        # TODO: set fake.should_fail = True before calling process_order
        # TODO: assert that result.success is False
        pass

    def test_multiple_orders_are_all_recorded(self) -> None:
        # TODO: call process_order twice with different orders
        # TODO: assert that fake.charged_payments has exactly two entries
        pass


@pytest.mark.payments
class TestCancelOrder:
    def test_successful_refund_returns_success_result(self) -> None:
        # TODO: call cancel_order with a valid transaction_id and positive amount
        # TODO: assert result.success is True
        fake_adapter = fake_payment_gateway.FakePaymentGateway()
        order_srv = order_service.OrderService(payment_gateway=fake_adapter)
        order = models.Order(
            order_id=str(uuid.uuid4()), amount=100.0, currency="USD", card_token="fake-card-token"
        )
        result_charge = order_srv.process_order(order=order)
        result_refund = order_srv.cancel_order(
            transaction_id=result_charge.transaction_id, amount=100.0
        )
        assert result_refund.message == "Refund successful"
        assert result_refund.success is True
        assert result_refund.transaction_id == result_charge.transaction_id

    def test_cancel_order_raises_when_amount_is_zero(self) -> None:
        # TODO: assert that cancel_order raises ValueError when amount=0
        pass

    def test_cancel_order_raises_when_amount_is_negative(self) -> None:
        # TODO: assert that cancel_order raises ValueError when amount is negative
        pass
