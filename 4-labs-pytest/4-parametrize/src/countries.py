class Country:
    """Representa un país con su nombre oficial y código ISO 3166-1 alpha-2."""

    def __init__(self, name: str, iso_code: str):
        self.name = name.strip()
        self.iso_code = iso_code.strip().upper()

    def __repr__(self) -> str:
        return f"Country(name={self.name!r}, iso_code={self.iso_code!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Country):
            return NotImplemented
        return self.iso_code == other.iso_code


# ---------------------------------------------------------------------------
# Catálogo interno  (30 países)
# ---------------------------------------------------------------------------

_CATALOG: list[Country] = [
    Country("Colombia", "CO"),
    Country("Mexico", "MX"),
    Country("Argentina", "AR"),
    Country("Brazil", "BR"),
    Country("Chile", "CL"),
    Country("Peru", "PE"),
    Country("Venezuela", "VE"),
    Country("Ecuador", "ECU"),
    Country("Bolivia", "BO"),
    Country("Paraguay", "PY"),
    Country("United States", "US"),
    Country("Canada", "CA"),
    Country("United Kingdom", "GB"),
    Country("Germany", "DE"),
    Country("France", "FR"),
    Country("Spain", "ES"),
    Country("Italy", "IT"),
    Country("Portugal", "PT"),
    Country("Netherlands", "NL"),
    Country("Sweden", "SE"),
    Country("Japan", "JP"),
    Country("China", "CN"),
    Country("India", "IN"),
    Country("South Korea", "KR"),
    Country("Australia", "AU"),
    Country("South Africa", "ZA"),
    Country("Nigeria", "NG"),
    Country("Egypt", "EG"),
    Country("Morocco", "MA"),
    Country("Saudi Arabia", "SA"),
]

_INDEX_BY_NAME: dict[str, Country] = {c.name.lower(): c for c in _CATALOG}

# ---------------------------------------------------------------------------
# Función principal
# ---------------------------------------------------------------------------


def get_iso_code(country_name: str) -> str:
    """
    Recibe el nombre de un país y retorna su código ISO 3166-1 alpha-2.

    La búsqueda es insensible a mayúsculas/minúsculas.

    Args:
        country_name: nombre del país en inglés (ej. "Colombia", "japan").

    Returns:
        Código ISO en mayúsculas (ej. "CO", "JP").

    Raises:
        ValueError:  si country_name está vacío o es solo espacios.
        KeyError:    si el país no existe en el catálogo.

    Ejemplos:
        get_iso_code("Colombia")      -> "CO"
        get_iso_code("japan")         -> "JP"
        get_iso_code("FRANCE")        -> "FR"
        get_iso_code("mars")          -> KeyError
        get_iso_code("")              -> ValueError
    """
    if not country_name or not country_name.strip():
        raise ValueError("El nombre del país no puede estar vacío")

    key = country_name.strip().lower()
    if key not in _INDEX_BY_NAME:
        raise KeyError(f"País no encontrado en el catálogo: '{country_name}'")

    return _INDEX_BY_NAME[key].iso_code


def get_country(country_name: str) -> Country:
    """
    Recibe el nombre de un país y retorna el objeto Country correspondiente.

    Mismas reglas de búsqueda y excepciones que get_iso_code().
    """
    if not country_name or not country_name.strip():
        raise ValueError("El nombre del país no puede estar vacío")

    key = country_name.strip().lower()
    if key not in _INDEX_BY_NAME:
        raise KeyError(f"País no encontrado en el catálogo: '{country_name}'")

    return _INDEX_BY_NAME[key]


def list_all() -> list[Country]:
    """Retorna una copia de todos los países del catálogo."""
    return list(_CATALOG)
