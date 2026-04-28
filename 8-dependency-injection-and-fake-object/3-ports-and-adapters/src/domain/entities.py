from dataclasses import dataclass


@dataclass(frozen=True)
class Character:
    id: int
    name: str
    status: str
    species: str
    gender: str
    origin_name: str
