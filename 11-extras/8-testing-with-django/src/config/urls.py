from django.urls import URLPattern, URLResolver, include, path

urlpatterns: list[URLPattern | URLResolver] = [
    path("products/", include("products.urls", namespace="products")),
]
