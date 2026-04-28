import pytest
from src.users_and_orders import order, user, user_service


def get_fake_order() -> order.Order:
    return order.Order(order_name="fake", order_id="fake")


@pytest.fixture
def fxt_setup_user_and_order(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("src.users_and_orders.user_service.order.get_order", get_fake_order)
    monkeypatch.setattr(
        "src.users_and_orders.user_service.user.get_user",
        lambda: user.User(name="fake", last_name="fake"),
    )


def test_should_get_user_and_orders_related_to_user(fxt_setup_user_and_order: None) -> None:
    result = user_service.get_user_and_orders_related_to_user()
    assert isinstance(result, tuple)
