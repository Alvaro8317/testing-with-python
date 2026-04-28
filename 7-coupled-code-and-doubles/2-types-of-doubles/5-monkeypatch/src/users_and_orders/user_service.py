from src.users_and_orders import order, user


def get_user_and_orders_related_to_user() -> tuple:
    return (order.get_order(), user.get_user())
