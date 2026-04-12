"""
tests/test_score_tracker.py
=============================
Laboratorio: estrategias de prueba con enteros y flotantes.

Escribe un test por cada comportamiento descrito en los comentarios.
Importa lo que necesites desde src.score_tracker.
"""

import hypothesis
from hypothesis import strategies as st
from src import score_tracker

# ---------------------------------------------------------------------------
# add_points
# ---------------------------------------------------------------------------

# sumar 0 puntos no cambia el marcador
# sumar puntos positivos incrementa el marcador correctamente
# sumar puntos a un marcador de 0 retorna los puntos sumados
# sumar puntos negativos lanza ValueError


@hypothesis.given(current_score=st.integers(min_value=0, max_value=100), points_to_add=st.just(0))
def test_add_points_add_zero_points_should_not_change_the_score_tracker(
    current_score: int, points_to_add: int
) -> None:
    result = score_tracker.add_points(current_score=current_score, points=points_to_add)
    assert result == current_score


@hypothesis.given(
    current_score=st.integers(min_value=0, max_value=100),
    points_to_add=st.integers(min_value=1, max_value=10),
)
def test_add_points_should_update_the_current_score(current_score: int, points_to_add: int) -> None:
    result = score_tracker.add_points(current_score=current_score, points=points_to_add)
    assert result > current_score


# ---------------------------------------------------------------------------
# subtract_points
# ---------------------------------------------------------------------------

# restar menos puntos de los que hay reduce el marcador
# restar exactamente los puntos disponibles deja el marcador en 0
# restar más puntos de los que hay deja el marcador en 0 (no negativo)
# restar 0 puntos no cambia el marcador
# restar puntos negativos lanza ValueError


# ---------------------------------------------------------------------------
# is_tied
# ---------------------------------------------------------------------------

# dos marcadores iguales retorna True
# dos marcadores distintos retorna False
# dos marcadores en 0 retorna True


# ---------------------------------------------------------------------------
# winner
# ---------------------------------------------------------------------------

# cuando A tiene más puntos retorna 'A'
# cuando B tiene más puntos retorna 'B'
# cuando ambos tienen los mismos puntos retorna 'tie'
# cuando ambos tienen 0 puntos retorna 'tie'


# ---------------------------------------------------------------------------
# goal_difference
# ---------------------------------------------------------------------------

# la diferencia entre 5 y 3 es 2
# la diferencia entre 3 y 5 también es 2 (valor absoluto)
# la diferencia entre marcadores iguales es 0


# ---------------------------------------------------------------------------
# average_score
# ---------------------------------------------------------------------------

# el promedio de una lista de enteros iguales es ese mismo entero como float
# el promedio de [1, 2, 3] es 2.0
# el promedio de un único elemento es ese elemento como float
# el promedio de una lista vacía lanza ValueError
# el resultado es de tipo float


# ---------------------------------------------------------------------------
# highest_score
# ---------------------------------------------------------------------------

# retorna el mayor puntaje de la lista
# retorna el único elemento si la lista tiene uno solo
# funciona cuando el mayor está al inicio de la lista
# funciona cuando el mayor está al final de la lista
# lanza ValueError si la lista está vacía


# ---------------------------------------------------------------------------
# normalize_score
# ---------------------------------------------------------------------------

# normalizar el puntaje máximo retorna exactamente 1.0
# normalizar 0 retorna exactamente 0.0
# normalizar la mitad del máximo retorna aproximadamente 0.5
# el resultado es de tipo float
# lanza ValueError si max_score es 0


# ---------------------------------------------------------------------------
# winning_percentage
# ---------------------------------------------------------------------------

# ganar todos los partidos retorna 100.0
# no ganar ningún partido retorna 0.0
# ganar la mitad retorna 50.0
# el resultado es de tipo float
# lanza ValueError si total_games es 0
# lanza ValueError si wins supera total_games
