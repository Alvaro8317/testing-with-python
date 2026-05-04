from tests import mothers


def test_should_allow_customer_to_place_order_when_data_is_complete() -> None:
    customer = mothers.CustomerMother.default()

    assert customer.can_place_order() is True


def test_should_deny_customer_to_place_order_when_email_is_missing() -> None:
    customer = mothers.CustomerMother.without_email()

    assert customer.can_place_order() is False


def test_should_create_premium_customer_with_discount_flag() -> None:
    customer = mothers.CustomerMother.premium()

    assert customer.is_premium is True


def test_should_create_customer_with_custom_name() -> None:
    customer = mothers.CustomerMother.create(name="Alice Wonder")

    assert customer.name == "Alice Wonder"


def test_should_create_customer_with_custom_email() -> None:
    customer = mothers.CustomerMother.create(email="alice@example.com")

    assert customer.email == "alice@example.com"
