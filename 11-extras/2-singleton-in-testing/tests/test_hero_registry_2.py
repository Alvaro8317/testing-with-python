from src import hero_registry


def test_should_registry_starts_empty() -> None:
    setup_hero_registry()
    registry = hero_registry.HeroRegistry()

    # Pasa si corre primero
    # Falla si corre después de test_should_add_hero
    assert registry.count() == 0


def test_should_add_hero() -> None:
    setup_hero_registry()
    registry = hero_registry.HeroRegistry()
    registry.add("Spider-Man", 55)

    assert registry.get("Spider-Man") == 55
    assert registry.count() == 1  # Falla si ya había héroes de otro test


def test_should_not_found_hero() -> None:
    setup_hero_registry()
    registry = hero_registry.HeroRegistry()

    # Pasa si corre primero
    # Falla si test_agregar_heroe corrió antes
    assert registry.get("Spider-Man") is None


def setup_hero_registry() -> None:
    hero_registry.HeroRegistry._instance = None
    hero_registry.HeroRegistry._heroes = {}
