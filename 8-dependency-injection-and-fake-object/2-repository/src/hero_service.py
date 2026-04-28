from src import hero_repository


class HeroService:
    def __init__(self, repo: hero_repository.HeroRepository):
        self.repo = repo

    def recruit_hero(self, name: str, strength: int, city: str) -> dict:
        if strength < 0 or strength > 100:
            raise ValueError(f"La fuerza debe estar entre 0 y 100, se recibió {strength}")
        if not name.strip():
            raise ValueError("El nombre no puede estar vacío")
        return self.repo.save(name, strength, city)

    def get_strongest_in_city(self, city: str) -> dict | None:
        heroes = self.repo.get_by_city(city)
        if not heroes:
            return None
        return max(heroes, key=lambda h: h["strength"])

    def power_up(self, hero_id: int, bonus: int) -> dict | None:
        hero = self.repo.get_by_id(hero_id)
        if hero is None:
            return None
        new_strength = min(hero["strength"] + bonus, 100)
        return self.repo.update_strength(hero_id, new_strength)
