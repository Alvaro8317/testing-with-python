import hypothesis
from hypothesis import strategies as st
from src import purchase_product

product_strategy = st.builds(
    purchase_product.PurchaseProduct,
    price=st.floats(min_value=0.01, max_value=100_000),
    quantity=st.integers(min_value=1, max_value=100),
    percetaje_discount=st.floats(min_value=0.0, max_value=100),
)


@hypothesis.given(product_strategy)
def test_final_price_should_not_be_negative(product: purchase_product.PurchaseProduct) -> None:
    final_price = purchase_product.calculate_final_price(product=product)
    assert final_price >= 0
