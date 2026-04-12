from src import separated_code


def test_should_format_complete_name() -> None:
    usuario = separated_code.User(name="  ana garcía  ", email="ana@empresa.com")
    assert usuario.complete_name() == "Ana García"
