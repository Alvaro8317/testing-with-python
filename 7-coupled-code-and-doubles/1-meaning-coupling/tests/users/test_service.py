import pytest
from src.users import service


def test_should_throw_error_because_email_is_duplicated() -> None:
    user_service = service.UserService()
    # ^ esta línea ya ejecuta DatabaseConnection.__init__()
    # que intenta conectarse a prod_database.db
    # Si el archivo no existe de la base de datos, puede que cree esta misma base de datos
    # o si la tabla no está creada el test explota aquí, antes de llegar a la lógica
    user_service.register("Ana", "ana@empresa.com")

    with pytest.raises(ValueError):
        user_service.register("Otro", "ana@empresa.com")
