import os
import warnings

import pytest
from src import car_shopping

# --------------------- FIXTURES --------------------- #


@pytest.fixture
def fxt_car_shared_conftest() -> car_shopping.CarShopping:
    return car_shopping.CarShopping()


# --------------------- HOOKS --------------------- #


# def pytest_configure(config: pytest.Config) -> None:
#     config.addinivalue_line("markers", "slow: Marca los tests más lentos")
#     config.addinivalue_line("markers", "critical: Marca los tests más críticos del negocio")


def pytest_runtest_setup(item: pytest.Item) -> None:
    # print("Corriendo esta prueba: ", item.name)
    if item.name == "test_should_add_item_and_show_the_total":
        print(
            "Este test debería de tener un caso de uso en especial, "
            "como enviar o generar un reporte"
        )


def pytest_sessionstart(session: pytest.Session) -> None:
    print("Vamos a empezar a correr unos cuantos test.")


def pytest_sessionfinish(session: pytest.Session, exitstatus: pytest.ExitCode) -> None:
    print("Vamos a finalizar la ejecución de unos cuantos test.")


# --------------------- GLOBAL CONFIG --------------------- #


@pytest.fixture(autouse=True)
def ignore_deprecated_warnings() -> None:
    warnings.filterwarnings("ignore", category=DeprecationWarning)


@pytest.fixture(scope="session")
def configure_environment() -> dict[str, str | bool | int | None]:
    return {"env": os.getenv("APP_ENV"), "debug": True, "timetout": 30}
