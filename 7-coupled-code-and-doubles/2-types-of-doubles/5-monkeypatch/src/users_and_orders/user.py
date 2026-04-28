import dataclasses


@dataclasses.dataclass
class User:
    name: str
    last_name: str


def get_user() -> User:
    raise ConnectionError()
