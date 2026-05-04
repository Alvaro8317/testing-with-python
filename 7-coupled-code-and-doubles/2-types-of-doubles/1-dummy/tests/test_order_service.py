from unittest import mock

from src import order_service


# DummyLogger satisface la firma del constructor de OrderService,
# pero no hace nada. No nos importa el logging en este test.
class DummyLogger(order_service.Logger):
    def log(self, message: str) -> None:
        pass  # No hace nada — es un dummy


class TestOrderService:
    def test_calculate_total_returns_correct_value(self) -> None:
        dummy_logger = DummyLogger()  # Solo existe para pasar el argumento
        service = order_service.OrderService(logger=dummy_logger)
        order = order_service.Order(product="Laptop", quantity=3)

        total = service.calculate_total(order, price_per_unit=1000.0)

        assert total == 3000.0

    def test_calculate_total_with_zero_quantity(self) -> None:
        dummy_logger = DummyLogger()
        service = order_service.OrderService(logger=dummy_logger)
        order = order_service.Order(product="Mouse", quantity=0)

        total = service.calculate_total(order, price_per_unit=25.0)

        assert total == 0.0


def test_should_get_order_from_cache() -> None:
    service = order_service.OrderService(logger=DummyLogger())
    response_dummy = mock.MagicMock()
    result = service.get_order(id_order=1, http_response=response_dummy)
    assert result.quantity == 210
