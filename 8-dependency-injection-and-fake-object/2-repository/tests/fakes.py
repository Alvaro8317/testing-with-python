from src import hero_repository


class FakeHeroRepository(hero_repository.HeroRepository):
    def __init__(self, db_path: str = "heroes.db") -> None:
        self._store: dict[int, dict] = {}
        self._next_id: int = 1

    def save(self, name: str, strength: int, city: str) -> dict:
        hero = {"id": self._next_id, "name": name, "strength": strength, "city": city}
        self._store[self._next_id] = hero
        self._next_id += 1
        return hero

    def get_by_id(self, hero_id: int) -> dict | None:
        return self._store.get(hero_id)

    def get_by_city(self, city: str) -> list[dict]:
        heroes_by_city = [hero for hero in self._store.values() if hero["city"] == city]
        return heroes_by_city

    def delete(self, hero_id: int) -> bool:
        if hero_id in self._store:
            del self._store[hero_id]
            return True
        return False

    def update_strength(self, hero_id: int, strength: int) -> dict | None:
        if hero_id in self._store:
            self._store[hero_id] = {**self._store[hero_id], "strength": strength}
            return self._store[hero_id]
        return None
