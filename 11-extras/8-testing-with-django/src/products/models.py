from django.core import validators
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validators.MinValueValidator(0)],
    )
    stock = models.IntegerField(default=0, validators=[validators.MinValueValidator(0)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def is_available(self) -> bool:
        return self.is_active and self.stock > 0
