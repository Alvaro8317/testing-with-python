"""
src/score_tracker.py
=====================
Sistema de puntajes para una competencia deportiva.
Lleva el marcador de dos equipos y calcula estadísticas del partido.
"""


def add_points(current_score: int, points: int) -> int:
    """Suma puntos al marcador actual de un equipo."""
    if points < 0:
        raise ValueError("Los puntos a agregar no pueden ser negativos")
    return current_score + points


def subtract_points(current_score: int, points: int) -> int:
    """Resta puntos al marcador (penalización). El marcador mínimo es 0."""
    if points < 0:
        raise ValueError("Los puntos a restar no pueden ser negativos")
    result = current_score - points
    return result if result > 0 else 0


def is_tied(score_a: int, score_b: int) -> bool:
    """Retorna True si ambos equipos tienen el mismo puntaje."""
    return score_a == score_b


def winner(score_a: int, score_b: int) -> str:
    """
    Retorna 'A' si el equipo A va ganando, 'B' si va ganando B,
    o 'tie' si están empatados.
    """
    if score_a > score_b:
        return "A"
    if score_b > score_a:
        return "B"
    return "tie"


def goal_difference(score_a: int, score_b: int) -> int:
    """Retorna la diferencia absoluta de goles entre los dos equipos."""
    return abs(score_a - score_b)


def average_score(scores: list[int]) -> float:
    """
    Calcula el promedio de una lista de puntajes.
    Lanza ValueError si la lista está vacía.
    """
    if not scores:
        raise ValueError("La lista de puntajes no puede estar vacía")
    return sum(scores) / len(scores)


def highest_score(scores: list[int]) -> int:
    """
    Retorna el puntaje más alto de la lista.
    Lanza ValueError si la lista está vacía.
    """
    if not scores:
        raise ValueError("La lista de puntajes no puede estar vacía")
    return max(scores)


def normalize_score(score: int, max_score: int) -> float:
    """
    Normaliza un puntaje al rango [0.0, 1.0] respecto al máximo posible.
    Lanza ValueError si max_score es 0.
    """
    if max_score == 0:
        raise ValueError("El puntaje máximo no puede ser 0")
    return score / max_score


def winning_percentage(wins: int, total_games: int) -> float:
    """
    Calcula el porcentaje de victorias como valor entre 0.0 y 100.0.
    Lanza ValueError si total_games es 0 o negativo.
    Lanza ValueError si wins es mayor que total_games.
    """
    if total_games <= 0:
        raise ValueError("El total de partidos debe ser mayor a 0")
    if wins > total_games:
        raise ValueError("Las victorias no pueden superar el total de partidos")
    return (wins / total_games) * 100
