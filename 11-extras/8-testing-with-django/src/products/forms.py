from decimal import Decimal

from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "stock", "is_active"]

    def clean_name(self) -> str:
        name: str | None = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("Invalid name")
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long")
        return name

    def clean_price(self) -> Decimal:
        price: Decimal | None = self.cleaned_data.get("price")
        if not price:
            raise forms.ValidationError("Price must be valid")
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be greater than zero")
        return price
