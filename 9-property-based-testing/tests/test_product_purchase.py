import hypothesis
from hypothesis import strategies as st
from src import purchase_product


def test_should_give_discount_of_50_percent() -> None:
    product = purchase_product.PurchaseProduct(price=100.0, quantity=1, percetaje_discount=50.0)
    assert purchase_product.calculate_final_price(product=product) == 50.0


# 1. El precio final no puede ser mayor a lo que es precio * cantidad
# 2. El precio final NUNCA puede ser negativo
# 3. Con 0% de descuento, el precio final siempre debe de ser precio * cantidad
# 4. Con 100% de descuento, el precio final debe de ser 0


@hypothesis.given(
    price=st.floats(min_value=0.01, max_value=100_000),
    quantity=st.integers(min_value=1, max_value=100),
    percentaje_discount=st.floats(min_value=0, max_value=100),
)
def test_final_price_should_not_be_more_than_original_price(
    price: float, quantity: int, percentaje_discount: float
) -> None:
    product = purchase_product.PurchaseProduct(
        price=price, quantity=quantity, percetaje_discount=percentaje_discount
    )
    max_price = round(price * quantity, 2)
    assert purchase_product.calculate_final_price(product=product) <= max_price
