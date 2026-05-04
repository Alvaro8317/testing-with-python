import pytest
from django.test import Client
from django.urls import reverse
from products.models import Product


@pytest.mark.django_db
def test_should_return_200_on_product_list(client: Client) -> None:
    response = client.get(reverse("products:list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_list_only_active_products(
    client: Client, product: Product, inactive_product: Product
) -> None:
    response = client.get(reverse("products:list"))
    assert response.status_code == 200
    assert "Test Product" in response.content.decode()
    assert "Inactive Product" not in response.content.decode()


@pytest.mark.django_db
def test_should_return_empty_list_when_no_active_products_exist(
    client: Client, inactive_product: Product
) -> None:
    response = client.get(reverse("products:list"))
    assert response.status_code == 200
    assert "No products available" in response.content.decode()


@pytest.mark.django_db
def test_should_return_200_on_product_detail(client: Client, product: Product) -> None:
    response = client.get(reverse("products:detail", kwargs={"pk": product.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_display_product_name_on_detail_page(client: Client, product: Product) -> None:
    response = client.get(reverse("products:detail", kwargs={"pk": product.pk}))
    assert "Test Product" in response.content.decode()


@pytest.mark.django_db
def test_should_return_404_when_product_does_not_exist(client: Client) -> None:
    response = client.get(reverse("products:detail", kwargs={"pk": 99999}))
    assert response.status_code == 404


@pytest.mark.django_db
def test_should_return_200_on_product_create_get(client: Client) -> None:
    response = client.get(reverse("products:create"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_create_product_and_redirect_on_valid_post(client: Client) -> None:
    data = {"name": "New Laptop", "price": "1299.99", "stock": 5, "is_active": True}
    response = client.post(reverse("products:create"), data)
    assert response.status_code == 302
    assert Product.objects.filter(name="New Laptop").exists()


@pytest.mark.django_db
def test_should_redirect_to_product_detail_after_create(client: Client) -> None:
    data = {"name": "New Monitor", "price": "299.99", "stock": 3, "is_active": True}
    response = client.post(reverse("products:create"), data)
    created_product = Product.objects.get(name="New Monitor")
    assert response["Location"] == reverse("products:detail", kwargs={"pk": created_product.pk})


@pytest.mark.django_db
def test_should_not_create_product_on_invalid_post(client: Client) -> None:
    data = {"name": "AB", "price": "0.00", "stock": 0, "is_active": True}
    response = client.post(reverse("products:create"), data)
    assert response.status_code == 200
    assert not Product.objects.filter(name="AB").exists()


@pytest.mark.django_db
def test_should_not_create_product_when_name_is_missing(client: Client) -> None:
    initial_count: int = Product.objects.count()
    data = {"price": "99.99", "stock": 5, "is_active": True}
    client.post(reverse("products:create"), data)
    assert Product.objects.count() == initial_count
