from collections.abc import Generator

import pytest
from src import hero_registry


@pytest.fixture
def fxt_hero_registry() -> Generator[hero_registry.HeroRegistry]:
    registry = hero_registry.HeroRegistry()
    yield registry
    hero_registry.HeroRegistry._instance = None
    hero_registry.HeroRegistry._heroes = {}


def test_should_registry_starts_empty(fxt_hero_registry: hero_registry.HeroRegistry) -> None:
    assert fxt_hero_registry.count() == 0


def test_should_add_hero(fxt_hero_registry: hero_registry.HeroRegistry) -> None:
    fxt_hero_registry.add("Spider-Man", 55)

    assert fxt_hero_registry.get("Spider-Man") == 55
    assert fxt_hero_registry.count() == 1


def test_should_not_found_hero(fxt_hero_registry: hero_registry.HeroRegistry) -> None:
    assert fxt_hero_registry.get("Spider-Man") is None
