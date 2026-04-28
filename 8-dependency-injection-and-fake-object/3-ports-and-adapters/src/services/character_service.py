from src.domain import entities, ports


def get_character(adapter_character: ports.CharacterPort, character_id: int) -> entities.Character:
    return adapter_character.get_by_id(character_id=character_id)
