from collections.abc import Generator

import pytest
from src import shopping_cart

# ===========================================================================
# 1. HOOKS DE SESIÓN
# ===========================================================================


def pytest_configure(config: pytest.Config) -> None:
    """
    Hook que pytest llama al arrancar, antes de recolectar tests.
    Útil para registrar marcadores personalizados y evitar warnings.

    Lab: Registra dos marcadores nuevos, uno llamado laboratory y otro llamado udemy,
    con una descripción cualquiera
    """
    pass


def pytest_sessionstart(session: pytest.Session) -> None:
    """
    Hook que se ejecuta una sola vez al INICIO de la sesión de tests.
    Recibe el objeto `session` con la configuración global.

    Lab: Deja un mensaje que diga "🚀 Iniciando suite de tests del laboratorio de conftest 🚀"
    con saltos de línea
    """
    pass


def pytest_sessionfinish(session: pytest.Session, exitstatus: pytest.ExitCode) -> None:
    """
    Hook que se ejecuta una sola vez al FINAL de la sesión.
    `exitstatus` es 0 si todos los tests pasaron, distinto de 0 si hay fallos.

    Lab: Dejar un mensaje según como hayan terminado las pruebas.
    Todo OK: ✅ Sesión terminada con código de salida en 0 ✅
    Algún test falló: ❌ Sesión terminada con código de salida en error ❌
    """
    pass


def pytest_runtest_logreport(report: pytest.TestReport) -> None:
    """
    Hook que pytest llama después de cada fase de un test (setup / call / teardown).
    Aquí solo nos interesa la fase 'call' (ejecución real del test).

    Lab: Deja un print cuando el reporte sea de tipo "call" y el reporte "falle"
    """
    if report.when == "call" and report.failed:
        print(f"\n  ⚠️  FALLÓ: {report.nodeid}")


# ===========================================================================
# 2. FIXTURES
# ===========================================================================


@pytest.fixture(scope="session")
def fxt_product_catalog() -> dict[str, shopping_cart.Product]:
    """
    Catálogo de productos disponibles durante toda la sesión.
    Al ser scope='session', todos los módulos de test comparten la misma instancia.

    Úsalo cuando los datos son de solo lectura y construirlos es costoso.
    ⚠️  No mutarlo dentro de los tests — es compartido.
    """
    return {
        "laptop": shopping_cart.Product("Laptop", price=1_200.00, stock=10),
        "headphones": shopping_cart.Product("Headphones", price=80.00, stock=5),
        "usb_hub": shopping_cart.Product("USB Hub", price=25.00, stock=20),
        "webcam": shopping_cart.Product("Webcam", price=150.00, stock=3),
    }


@pytest.fixture
def fxt_empty_cart() -> Generator[shopping_cart.ShoppingCart]:
    """
    Carrito vacío. Se crea de nuevo para cada test (scope='function' por defecto).
    El bloque después del yield es el TEARDOWN: se ejecuta aunque el test falle.
    """
    cart = shopping_cart.ShoppingCart()
    yield cart
    # --- teardown ---
    cart.clear()


# ===========================================================================
# FIXTURES COMPUESTAS  (fixtures que usan otras fixtures)
# ===========================================================================


@pytest.fixture
def fxt_cart_with_items(
    fxt_empty_cart: shopping_cart.ShoppingCart,
    fxt_product_catalog: dict[str, shopping_cart.Product],
) -> shopping_cart.ShoppingCart:
    """
    Carrito pre-cargado con dos productos del catálogo.
    Ilustra que una fixture puede recibir otras fixtures como argumentos.

    Lab: Añadir dos productos del catalogo de productos
    """
    raise NotImplementedError()
