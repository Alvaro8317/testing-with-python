from decimal import Decimal

import pytest
from products import models


@pytest.mark.django_db
def test_should_create_product_with_valid_data() -> None:
    product = models.Product.objects.create(
        name="Laptop",
        price=Decimal("999.99"),
        stock=5,
    )
    assert product.pk is not None
    assert product.name == "Laptop"
    assert product.price == Decimal("999.99")
    assert product.stock == 5
    assert product.is_active is True


@pytest.mark.django_db
def test_should_set_is_active_true_by_default() -> None:
    product = models.Product.objects.create(name="Mouse", price=Decimal("29.99"), stock=1)
    assert product.is_active is True


@pytest.mark.django_db
def test_should_set_stock_zero_by_default() -> None:
    product = models.Product.objects.create(name="Keyboard", price=Decimal("49.99"))
    assert product.stock == 0


@pytest.mark.django_db
def test_should_mark_product_as_available_when_stock_is_positive(product: models.Product) -> None:
    assert product.is_available() is True


@pytest.mark.django_db
def test_should_mark_product_as_unavailable_when_stock_is_zero(
    out_of_stock_product: models.Product,
) -> None:
    assert out_of_stock_product.is_available() is False


@pytest.mark.django_db
def test_should_mark_product_as_unavailable_when_inactive(inactive_product: models.Product) -> None:
    assert inactive_product.is_available() is False


@pytest.mark.django_db
def test_should_mark_product_as_unavailable_when_inactive_and_out_of_stock() -> None:
    product = models.Product.objects.create(
        name="Ghost Product",
        price=Decimal("9.99"),
        stock=0,
        is_active=False,
    )
    assert product.is_available() is False


@pytest.mark.django_db
def test_should_return_product_name_as_string_representation(product: models.Product) -> None:
    assert str(product) == "Test Product"


@pytest.mark.django_db
def test_should_persist_product_in_database() -> None:
    models.Product.objects.create(name="Monitor", price=Decimal("299.99"), stock=3)
    assert models.Product.objects.filter(name="Monitor").exists()


@pytest.mark.django_db
def test_should_retrieve_product_by_name() -> None:
    models.Product.objects.create(name="Webcam", price=Decimal("79.99"), stock=2)
    result = models.Product.objects.get(name="Webcam")
    assert result.price == Decimal("79.99")
