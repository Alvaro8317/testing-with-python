import requests

BASE_URL = "https://superheroapi2.com/api/TOKEN"


def get_character(character_id: int) -> dict:
    response = requests.get(f"{BASE_URL}/{character_id}")
    response.raise_for_status()
    return response.json()


def get_power_stats(character_id: int) -> dict:
    data = get_character(character_id)
    return {
        "name": data["name"],
        "intelligence": int(data["powerstats"]["intelligence"]),
        "strength": int(data["powerstats"]["strength"]),
        "speed": int(data["powerstats"]["speed"]),
    }


def is_stronger_than(character_id: int, strength_threshold: int) -> bool:
    stats = get_power_stats(character_id)
    return stats["strength"] > strength_threshold
