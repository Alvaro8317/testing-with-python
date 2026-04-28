import abc

from src.domain import entities


class CharacterPort(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, character_id: int) -> entities.Character:
        raise NotImplementedError
