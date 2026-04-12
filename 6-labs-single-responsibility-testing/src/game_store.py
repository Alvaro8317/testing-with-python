"""
Tienda de videojuegos estilo Steam.

Este módulo tiene TRES responsabilidades mezcladas en una sola clase:

    1. Gestión del catálogo      → agregar, buscar y listar juegos
    2. Gestión del carrito       → agregar, quitar y calcular totales
    3. Aplicación de descuentos  → cupones y descuentos por categoría

Tu laboratorio tiene dos partes:

    PARTE 1 — Escribe los tests unitarios para GameStore tal como está.
              Notarás que para probar descuentos necesitas primero
              construir un catálogo Y un carrito. Para probar el carrito
              necesitas que el catálogo ya tenga juegos. Todo está acoplado.

    PARTE 2 — Refactoriza src/ dividiendo GameStore en tres módulos con
              una sola responsabilidad cada uno. Luego reescribe los tests.
              Compara cuánto más fácil es probar cada pieza por separado.
"""

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


class GameStore:
    """
    Tienda de videojuegos con catálogo, carrito y sistema de descuentos.

    Responsabilidad 1 — Catálogo:
        add_to_catalog, get_game, list_by_genre, search

    Responsabilidad 2 — Carrito:
        add_to_cart, remove_from_cart, cart_total, cart_item_count, clear_cart

    Responsabilidad 3 — Descuentos:
        apply_coupon, discount_by_genre, final_total
    """

    # Cupones válidos: { codigo: porcentaje_de_descuento }
    VALID_COUPONS: dict[str, float] = {
        "STEAM2025": 0.10,
        "INDIE20": 0.20,
        "BLACKfriday": 0.30,
    }

    def __init__(self) -> None:
        self._catalog: dict[str, Game] = {}
        self._cart: list[Game] = []
        self._used_coupons: set[str] = set()
        self._active_coupon: str | None = None

    # ------------------------------------------------------------------
    # Responsabilidad 1: Catálogo
    # ------------------------------------------------------------------

    def add_to_catalog(self, game: Game) -> None:
        """
        Agrega un juego al catálogo.
        Lanza ValueError si ya existe un juego con el mismo título.
        """
        if game.title in self._catalog:
            raise ValueError(f"'{game.title}' ya está en el catálogo")
        self._catalog[game.title] = game

    def get_game(self, title: str) -> Game:
        """
        Retorna un juego del catálogo por título.
        Lanza GameNotFoundError si no existe.
        """
        if title not in self._catalog:
            raise GameNotFoundError(f"'{title}' no está en el catálogo")
        return self._catalog[title]

    def list_by_genre(self, genre: str) -> list[Game]:
        """Retorna todos los juegos de un género, ordenados por rating descendente."""
        return sorted(
            [g for g in self._catalog.values() if g.genre.lower() == genre.lower()],
            key=lambda g: g.rating,
            reverse=True,
        )

    def search(self, query: str) -> list[Game]:
        """
        Busca juegos cuyo título contenga el query (case-insensitive).
        Retorna lista vacía si no hay coincidencias.
        """
        q = query.lower()
        return [g for g in self._catalog.values() if q in g.title.lower()]

    def catalog_size(self) -> int:
        return len(self._catalog)

    # ------------------------------------------------------------------
    # Responsabilidad 2: Carrito
    # ------------------------------------------------------------------

    def add_to_cart(self, title: str) -> None:
        """
        Agrega un juego del catálogo al carrito.
        Lanza GameNotFoundError       si el juego no está en el catálogo.
        Lanza GameAlreadyInCartError  si el juego ya está en el carrito.
        """
        game = self.get_game(title)
        if game in self._cart:
            raise GameAlreadyInCartError(f"'{title}' ya está en el carrito")
        self._cart.append(game)

    def remove_from_cart(self, title: str) -> None:
        """
        Retira un juego del carrito.
        Lanza GameNotInCartError si el juego no está en el carrito.
        """
        game = self.get_game(title)
        if game not in self._cart:
            raise GameNotInCartError(f"'{title}' no está en el carrito")
        self._cart.remove(game)

    def cart_total(self) -> float:
        """Retorna la suma de precios de todos los juegos en el carrito."""
        return sum(g.price for g in self._cart)

    def cart_item_count(self) -> int:
        return len(self._cart)

    def clear_cart(self) -> None:
        self._cart.clear()
        self._active_coupon = None

    # ------------------------------------------------------------------
    # Responsabilidad 3: Descuentos
    # ------------------------------------------------------------------

    def apply_coupon(self, code: str) -> float:
        """
        Activa un cupón de descuento para la compra actual.
        Retorna el porcentaje de descuento aplicado.

        Lanza InvalidCouponError si el código no existe o ya fue usado.
        """
        if code not in self.VALID_COUPONS:
            raise InvalidCouponError(f"El cupón '{code}' no es válido")
        if code in self._used_coupons:
            raise InvalidCouponError(f"El cupón '{code}' ya fue usado")
        self._active_coupon = code
        return self.VALID_COUPONS[code]

    def discount_by_genre(self, genre: str) -> float:
        """
        Calcula el descuento total aplicable a los juegos de un género en el carrito.
        Los juegos de RPG tienen 15% de descuento adicional por género.
        Los juegos de Indie tienen 10% de descuento adicional por género.
        Cualquier otro género no tiene descuento por género.

        Retorna el monto en USD a descontar (no el porcentaje).
        """
        genre_discounts = {"RPG": 0.15, "Indie": 0.10}
        rate = genre_discounts.get(genre, 0.0)
        return sum(g.price * rate for g in self._cart if g.genre == genre)

    def final_total(self) -> float:
        """
        Calcula el total final del carrito aplicando:
            1. Descuento por cupón activo (sobre el total completo).
            2. Descuentos por género (sobre cada juego aplicable).

        El total nunca puede ser negativo.
        """
        base = self.cart_total()

        coupon_discount = 0.0
        if self._active_coupon:
            coupon_discount = base * self.VALID_COUPONS[self._active_coupon]

        genre_discount = self.discount_by_genre("RPG") + self.discount_by_genre("Indie")

        total = base - coupon_discount - genre_discount
        return max(0.0, total)
