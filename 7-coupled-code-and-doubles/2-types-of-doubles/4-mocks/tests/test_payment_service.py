from unittest import mock

from src import payment_service

# --- MOCKS con unittest.mock ---
# MagicMock crea un objeto que registra llamadas Y permite definir expectativas.
# Usamos assert_called_once_with, assert_called_with, etc.
# para verificar que la interacción fue exactamente la esperada.


@mock.patch("src.payment_service.payment_gateway.PaymentGateway")
def test_process_order_payment(mock_payment_gateway: mock.MagicMock) -> None:
    # Setup
    mock_payment_gateway_instance = mock_payment_gateway.return_value
    mock_payment_gateway_instance.charge.return_value = {"status": "Finished", "code": 201}

    service = payment_service.PaymentService()
    result = service.process_order_payment(card_token="fake-card-token", amount=20.0)
    assert result.get("status") == "Finished"
    mock_payment_gateway_instance.charge.assert_called_once_with(
        card_token="fake-card-token", amount=20.0, currency="USD"
    )


@mock.patch("src.payment_service.payment_gateway.PaymentGateway")
def test_process_cancel_order(mock_payment_gateway: mock.MagicMock) -> None:
    # Setup
    mock_payment_gateway_instance: mock.MagicMock = mock_payment_gateway.return_value
    mock_payment_gateway_instance.refund.return_value = {"status": "OK", "code": 201}

    service = payment_service.PaymentService()
    result = service.cancel_order(transaction_id="fake-transaction-id", amount=20.0)
    assert result.get("status") == "OK"
    mock_payment_gateway_instance.refund.assert_called_once()
