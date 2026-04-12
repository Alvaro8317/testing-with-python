from src import models


class CatalogGames:
    def __init__(self) -> None:
        self._catalog: dict[str, models.Game] = {}
        self._cart: list[models.Game] = []
        self._used_coupons: set[str] = set()
        self._active_coupon: str | None = None

    def add_to_catalog(self, game: models.Game) -> None:
        """
        Agrega un juego al catálogo.
        Lanza ValueError si ya existe un juego con el mismo título.
        """
        if game.title in self._catalog:
            raise ValueError(f"'{game.title}' ya está en el catálogo")
        self._catalog[game.title] = game

    def get_game(self, title: str) -> models.Game:
        """
        Retorna un juego del catálogo por título.
        Lanza GameNotFoundError si no existe.
        """
        if title not in self._catalog:
            raise models.GameNotFoundError(f"'{title}' no está en el catálogo")
        return self._catalog[title]

    def list_by_genre(self, genre: str) -> list[models.Game]:
        """Retorna todos los juegos de un género, ordenados por rating descendente."""
        return sorted(
            [g for g in self._catalog.values() if g.genre.lower() == genre.lower()],
            key=lambda g: g.rating,
            reverse=True,
        )

    def search(self, query: str) -> list[models.Game]:
        """
        Busca juegos cuyo título contenga el query (case-insensitive).
        Retorna lista vacía si no hay coincidencias.
        """
        q = query.lower()
        return [g for g in self._catalog.values() if q in g.title.lower()]

    def catalog_size(self) -> int:
        return len(self._catalog)
