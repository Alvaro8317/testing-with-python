import pytest
from src.adapters import rick_and_morty
from src.services import character_service


def test_should_get_character() -> None:
    result = character_service.get_character(
        adapter_character=rick_and_morty.FakeRickAndMortyApiAdapter(), character_id=1
    )
    assert result.id == 1


def test_should_raise_exception_character_not_found() -> None:
    with pytest.raises(rick_and_morty.CharacterNotFoundException) as exception_info:
        character_service.get_character(
            adapter_character=rick_and_morty.FakeRickAndMortyApiAdapter(), character_id=100
        )
    assert exception_info.type is rick_and_morty.CharacterNotFoundException
