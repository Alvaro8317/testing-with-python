from products import forms


def test_should_validate_form_with_valid_data() -> None:
    data = {"name": "Laptop", "price": "999.99", "stock": 5, "is_active": True}
    form = forms.ProductForm(data=data)
    assert form.is_valid()


def test_should_reject_name_shorter_than_three_characters() -> None:
    data = {"name": "PC", "price": "999.99", "stock": 5, "is_active": True}
    form = forms.ProductForm(data=data)
    assert not form.is_valid()
    assert "name" in form.errors


def test_should_accept_name_with_exactly_three_characters() -> None:
    data = {"name": "USB", "price": "9.99", "stock": 1, "is_active": True}
    form = forms.ProductForm(data=data)
    assert form.is_valid()


def test_should_reject_price_equal_to_zero() -> None:
    data = {"name": "Free Product", "price": "0.00", "stock": 5, "is_active": True}
    form = forms.ProductForm(data=data)
    assert not form.is_valid()
    assert "price" in form.errors


def test_should_reject_price_below_zero() -> None:
    data = {"name": "Negative Product", "price": "-10.00", "stock": 5, "is_active": True}
    form = forms.ProductForm(data=data)
    assert not form.is_valid()
    assert "price" in form.errors


def test_should_reject_missing_name() -> None:
    data = {"price": "99.99", "stock": 5, "is_active": True}
    form = forms.ProductForm(data=data)
    assert not form.is_valid()
    assert "name" in form.errors


def test_should_reject_missing_price() -> None:
    data = {"name": "Laptop", "stock": 5, "is_active": True}
    form = forms.ProductForm(data=data)
    assert not form.is_valid()
    assert "price" in form.errors


def test_should_default_stock_to_zero_when_not_provided() -> None:
    data = {"name": "Laptop", "price": "999.99", "is_active": True}
    form = forms.ProductForm(data=data)
    assert not form.is_valid()


def test_should_accept_product_without_is_active_field() -> None:
    data = {"name": "Laptop", "price": "999.99", "stock": 0}
    form = forms.ProductForm(data=data)
    assert form.is_valid()
    assert form.cleaned_data["is_active"] is False
