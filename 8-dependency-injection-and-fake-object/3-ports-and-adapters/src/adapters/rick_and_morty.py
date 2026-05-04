import requests

from src.domain import entities, ports


class CharacterNotFoundException(Exception): ...


class RickAndMortyApiAdapter(ports.CharacterPort):
    BASE_URL = "https://rickandmortyapi.com/api"

    def get_by_id(self, character_id: int) -> entities.Character:
        response = requests.get(
            f"{self.BASE_URL}/character/{character_id}",
            timeout=10,
        )
        data = response.json()
        if not data:
            raise CharacterNotFoundException(character_id)
        response.raise_for_status()

        return entities.Character(
            id=data["id"],
            name=data["name"],
            status=data["status"],
            species=data["species"],
            gender=data["gender"],
            origin_name=data["origin"]["name"],
        )
    
    def create_character(self) -> None:
        pass


class FakeRickAndMortyApiAdapter(ports.CharacterPort):
    _FAKE_STORAGE = {
        1: entities.Character(
            id=1,
            name="Rick Sanchez",
            status="Alive",
            species="Human",
            gender="Male",
            origin_name="Earth (C-137)",
        ),
        2: entities.Character(
            id=2,
            name="Morty Smith",
            status="Alive",
            species="Human",
            gender="Male",
            origin_name="unknown",
        ),
        3: entities.Character(
            id=3,
            name="Summer Smith",
            status="Alive",
            species="Human",
            gender="Female",
            origin_name="Earth (Replacement Dimension)",
        ),
    }

    def get_by_id(self, character_id: int) -> entities.Character:
        character_to_return = self._FAKE_STORAGE.get(character_id)
        if not character_to_return:
            raise CharacterNotFoundException(character_id)
        return character_to_return
