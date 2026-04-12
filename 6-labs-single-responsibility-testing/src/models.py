import dataclasses


class GameNotFoundError(Exception):
    """El juego no existe en el catálogo."""


class GameAlreadyInCartError(Exception):
    """El juego ya está en el carrito."""


class GameNotInCartError(Exception):
    """El juego no está en el carrito."""


class InvalidCouponError(Exception):
    """El cupón no es válido o ya fue usado."""


@dataclasses.dataclass
class Game:
    title: str
    genre: str
    price: float
    rating: float  # 0.0 – 5.0

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("El precio no puede ser negativo")
        if not (0.0 <= self.rating <= 5.0):
            raise ValueError("El rating debe estar entre 0.0 y 5.0")
