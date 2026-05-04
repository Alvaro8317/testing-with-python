from decimal import Decimal

import pytest
from products import models


@pytest.fixture
def product(db: None) -> models.Product:
    return models.Product.objects.create(
        name="Test Product",
        price=Decimal("99.99"),
        stock=10,
        is_active=True,
    )


@pytest.fixture
def inactive_product(db: None) -> models.Product:
    return models.Product.objects.create(
        name="Inactive Product",
        price=Decimal("49.99"),
        stock=0,
        is_active=False,
    )


@pytest.fixture
def out_of_stock_product(db: None) -> models.Product:
    return models.Product.objects.create(
        name="Out of Stock Product",
        price=Decimal("29.99"),
        stock=0,
        is_active=True,
    )
