from src.adapters import rick_and_morty
from src.services import character_service


def main() -> None:
    adapter = rick_and_morty.RickAndMortyApiAdapter()
    character = character_service.get_character(adapter_character=adapter, character_id=3)

    print(character)


if __name__ == "__main__":
    main()
