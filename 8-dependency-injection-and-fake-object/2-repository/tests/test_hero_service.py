import pytest
from src import hero_service

from tests import fakes


@pytest.fixture
def fxt_hero_service() -> hero_service.HeroService:
    return hero_service.HeroService(repo=fakes.FakeHeroRepository())


def test_should_recruit_hero(fxt_hero_service: hero_service.HeroService) -> None:
    result = fxt_hero_service.recruit_hero(name="Spiderman", strength=8, city="California")
    assert result.get("id") == 1
    result = fxt_hero_service.recruit_hero(name="Batman", strength=9, city="Gotham city")
    assert result.get("id") == 2


def test_should_get_strongest_in_city(fxt_hero_service: hero_service.HeroService) -> None:
    fxt_hero_service.recruit_hero(name="Batman", strength=9, city="Gotham city")
    fxt_hero_service.recruit_hero(name="Joker", strength=7, city="Gotham city")
    fxt_hero_service.recruit_hero(name="Superman", strength=10, city="Gotham city")
    result = fxt_hero_service.get_strongest_in_city("Gotham city")
    assert result
    assert result.get("id") == 3


def test_should_power_up(fxt_hero_service: hero_service.HeroService) -> None:
    result_creation = fxt_hero_service.recruit_hero(name="Bakugo", strength=6, city="Japan")
    result_power_up = fxt_hero_service.power_up(hero_id=result_creation["id"], bonus=2)
    assert result_power_up
    assert result_power_up.get("strength") == 8
