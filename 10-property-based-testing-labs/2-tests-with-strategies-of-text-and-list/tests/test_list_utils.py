import hypothesis
import pytest
from hypothesis import strategies as st
from src import list_utils

# ===========================================================================
# LISTAS — remove_duplicates
# ===========================================================================

# PROPIEDAD: el resultado nunca tiene más elementos que la lista original.
# ¿Por qué no un unit test? Tu ejemplo podría no tener duplicados
# y el test pasaría sin probar nada real.


@pytest.mark.list_utils
@hypothesis.given(st.lists(st.integers()))
def test_remove_duplicate_length_should_not_be_more_than_original(list_to_text: list[int]) -> None:
    result = list_utils.remove_duplicates(items=list_to_text)
    assert len(result) <= len(list_to_text)


# PROPIEDAD: cada elemento de la lista original aparece al menos una vez
# en el resultado (no se pierden elementos, solo se eliminan copias).


# PROPIEDAD: el resultado no tiene duplicados: convertirlo a set y comparar
# su longitud con la longitud del resultado siempre debe ser igual.
# ¿Por qué no un unit test? Solo Hypothesis puede generar listas con
# duplicados en posiciones y frecuencias que no se te ocurrirían manualmente.


# ===========================================================================
# LISTAS — flatten
# ===========================================================================

# PROPIEDAD: la cantidad total de elementos en el resultado es igual a la
# suma de los len() de cada sublista. Flatten no debe perder ni agregar elementos.
# ¿Por qué no un unit test? Con un caso fijo nunca sabes si la implementación
# funciona cuando hay sublistas vacías intercaladas, o listas de un solo elemento.


# PROPIEDAD: flatten([[]] * n) siempre retorna [] para cualquier n.
# Es decir, aplanar cualquier cantidad de listas vacías da una lista vacía.


# ===========================================================================
# LISTAS — chunk
# ===========================================================================

# PROPIEDAD: re-ensamblar los chunks con flatten produce la lista original.
# Esta es la propiedad de "roundtrip": chunk parte y flatten reconstruye.
# ¿Por qué no un unit test? El roundtrip debe funcionar para cualquier lista
# y cualquier tamaño de chunk, no solo para los que tú escribiste.


# PROPIEDAD: ningún chunk tiene más elementos que size.
# Hypothesis puede generar listas donde el último chunk exactamente llena
# o exactamente sobra — casos límite que un unit test rara vez atrapa.


# ===========================================================================
# LISTAS — top_n
# ===========================================================================

# PROPIEDAD: el resultado siempre está ordenado de mayor a menor.
# ¿Por qué no un unit test? Tu ejemplo podría estar ordenado por casualidad.
# Hypothesis genera listas en cualquier orden y con valores repetidos.


# PROPIEDAD: todos los elementos del resultado están en la lista original.
# Garantiza que top_n no inventa elementos.


# PROPIEDAD: el resultado nunca tiene más elementos que la lista original,
# sin importar qué n se pida.
