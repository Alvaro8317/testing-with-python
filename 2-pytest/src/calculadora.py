def divide(a: int, b: int) -> int | float:
    if b == 0:
        raise ValueError("You cant divide by zero")
    return a / b
