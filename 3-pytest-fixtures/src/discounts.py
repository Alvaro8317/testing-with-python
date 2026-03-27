import pydantic


class ProductPurchase(pydantic.BaseModel):
    price: float = pydantic.Field(gt=0, description="Price should be major than zero")
    quantity: int = pydantic.Field(ge=1, le=100, description="Between 1 and 100 units")
    percentaje_discount: float = pydantic.Field(
        ge=0, le=100, description="Discound must be between 0 and 100"
    )


def calculate_final_price(product: ProductPurchase) -> float:
    discount = product.price * (product.percentaje_discount) / 100
    return round((product.price - discount) * product.quantity, 2)
