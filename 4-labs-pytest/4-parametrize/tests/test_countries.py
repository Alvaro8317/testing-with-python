import pytest
from src import countries

# ===========================================================================
# SECCIÓN 1 — get_iso_code: casos válidos
#
# Escribe UN solo test parametrizado que verifique al menos 10 países.
# La tabla debe tener la forma:
#
#     (nombre_del_pais, codigo_iso_esperado)
#
# Requisitos mínimos:
#   ✅ Al menos 10 entradas en la tabla.
#   ✅ Incluir países de al menos 3 continentes distintos.
#   ✅ Incluir al menos un caso con nombre en minúsculas (ej. "japan").
#   ✅ Incluir al menos un caso con nombre en mayúsculas (ej. "FRANCE").
#   ✅ Incluir al menos un caso con capitalización normal (ej. "Colombia").
#   ✅ Incluir al menos un caso con con capitalización extraordinaria (ej. "MeXiCo").
# ===========================================================================


# TODO: completa la tabla con al menos 10 entradas usando pytest.param e
# indicando un id por cada caso de uso
@pytest.mark.parametrize(
    "country_name, expected_iso",
    [
        pytest.param("Colombia", "CO", id="Validation with Colombia"),
        pytest.param("Canada", "CA", id="Validation with Canada"),
        pytest.param("FRANCE", "FR", id="Validation with France"),
        pytest.param("MeXiCo", "MX", id="Validation with Mexico"),
        pytest.param("Ecuador", "EC", id="Validation with Ecuador"),
    ],
)
def test_get_iso_code_valid(country_name: str, expected_iso: str) -> None:
    assert countries.get_iso_code(country_name) == expected_iso


# ===========================================================================
# SECCIÓN 2 — get_iso_code: casos que deben lanzar excepción
#
# Escribe UN solo test parametrizado que verifique todos los casos de error.
# La tabla debe tener la forma:
#
#     (entrada_invalida, tipo_de_excepcion)
#
# Casos obligatorios:
#   - ""           → ValueError   (cadena vacía)
#   - "   "        → ValueError   (solo espacios)
#   - "Wakanda"    → KeyError     (país inventado)
#   - "Narnia"     → KeyError     (otro país inventado)
#   - "Krypton"    → KeyError     (otro más)
# ===========================================================================


# TODO: completa la tabla
@pytest.mark.parametrize(
    "country_name, expected_exception",
    [],
)
def test_get_iso_code_raises(country_name: str, expected_exception: type[Exception]) -> None:
    with pytest.raises(expected_exception):
        countries.get_iso_code(country_name)


# ===========================================================================
# SECCIÓN 3 — Country.__eq__
#
# Dos instancias de Country son iguales si tienen el mismo iso_code.
# Escribe un test parametrizado que verifique esto con al menos 4 pares.
#
# La tabla debe tener la forma:
#
#     (iso_a, iso_b, son_iguales)
#
# Sugerencia de casos:
#   - ("CO", "CO", True)   → mismo código
#   - ("CO", "MX", False)  → distintos
#   - ("US", "US", True)
#   - ("FR", "DE", False)
# ===========================================================================


# TODO: completa la tabla
@pytest.mark.parametrize("iso_a, iso_b, expected", [])
def test_country_equality(iso_a: str, iso_b: str, expected: bool) -> None:
    country_a = countries.Country("País A", iso_a)
    country_b = countries.Country("País B", iso_b)
    assert (country_a == country_b) is expected


# ===========================================================================
# SECCIÓN 4 — get_country: objeto retornado
#
# get_country() retorna un objeto Country con .name e .iso_code correctos.
# Escribe un test parametrizado con al menos 4 países que verifique
# que el iso_code del objeto retornado es el esperado.
#
# La tabla:  (nombre, iso_esperado)
# ===========================================================================


# TODO: completa la tabla
@pytest.mark.parametrize("country_name, expected_iso", [])
def test_get_country_returns_correct_object(country_name: str, expected_iso: str) -> None:
    country = countries.get_country(country_name)
    assert isinstance(country, countries.Country)
    assert country.iso_code == expected_iso


# ===========================================================================
# SECCIÓN 5 — list_all
#
# list_all() retorna la lista completa del catálogo.
# Estos tres tests NO requieren parametrize — son afirmaciones globales.
# Completa los asserts.
# ===========================================================================


def test_list_all_returns_30_countries() -> None:
    # TODO: verificar que list_all() retorna exactamente 30 países
    pass


def test_list_all_returns_country_instances() -> None:
    # TODO: verificar que todos los elementos son instancias de Country
    pass


def test_list_all_returns_a_copy() -> None:
    # TODO: verificar que mutar la lista retornada no afecta el catálogo interno
    # Pista: llama list_all() una vez, modificas la lista añadiendo un país inventado
    # llama list_all() nuevamente y compara si se modificó la lista de países original
    pass
