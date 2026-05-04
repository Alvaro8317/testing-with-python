import pytest
from src import hero_registry


@pytest.fixture(autouse=True)
def fxt_reset_singleton(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(hero_registry.HeroRegistry, "_instance", None)
    monkeypatch.setattr(hero_registry.HeroRegistry, "_heroes", {})


def test_should_registry_starts_empty() -> None:
    registry = hero_registry.HeroRegistry()

    assert registry.count() == 0


def test_should_add_hero() -> None:
    registry = hero_registry.HeroRegistry()
    registry.add("Spider-Man", 55)

    assert registry.get("Spider-Man") == 55
    assert registry.count() == 1


def test_should_not_found_hero() -> None:
    registry = hero_registry.HeroRegistry()

    assert registry.get("Spider-Man") is None
