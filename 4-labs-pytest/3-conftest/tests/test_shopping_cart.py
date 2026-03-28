from src import shopping_cart


def test_should_cart_starts_empty(fxt_empty_cart: shopping_cart.ShoppingCart) -> None:
    # TODO: verificar que el carrito recién creado está vacío
    pass


def test_should_add_product_increases_item_count(
    fxt_empty_cart: shopping_cart.ShoppingCart,
    fxt_product_catalog: dict[str, shopping_cart.Product],
) -> None:
    # TODO: agregar un producto y verificar que item_count cambia
    pass


def test_should_add_product_updates_total(
    fxt_empty_cart: shopping_cart.ShoppingCart,
    fxt_product_catalog: dict[str, shopping_cart.Product],
) -> None:
    # TODO: agregar laptop x2 y verificar que total == laptop.price * 2
    pass


def test_should_validate_that_a_car_already_has_products(
    fxt_cart_with_items: shopping_cart.ShoppingCart,
) -> None:
    # TODO: Ya hay unos productos en el carro
    pass
