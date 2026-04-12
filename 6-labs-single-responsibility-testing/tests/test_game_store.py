"""
PARTE 1 — Tests sobre GameStore tal como está
----------------------------------------------
Escribe un test por cada comportamiento listado en los comentarios.
Usa esta lista de juegos como datos de prueba — son títulos reales
lanzados recientemente que puedes encontrar en Steam:

    Game("Clair Obscur: Expedition 33", genre="RPG",   price=39.99, rating=4.9)
    Game("Split Fiction",               genre="Indie",  price=29.99, rating=4.8)
    Game("Elden Ring: Nightreign",      genre="RPG",   price=39.99, rating=4.7)
    Game("Hades 2",                     genre="Indie",  price=24.99, rating=4.8)
    Game("Ninja Gaiden 4",              genre="Action", price=34.99, rating=4.5)
    Game("Forza Horizon 6",             genre="Racing", price=59.99, rating=4.6)

    Notarás que para probar el carrito primero necesitas poblar el catálogo.
    Para probar los descuentos necesitas el catálogo Y el carrito.
    Anota esa fricción — es el punto central de la Parte 2.
"""

import pytest
from src import game_store

# ==========================================================================
# PARTE 1 — Escribe los tests
# ==========================================================================

# --------------------------------------------------------------------------
# Game (modelo)
# --------------------------------------------------------------------------

# un juego con precio negativo lanza ValueError
# un juego con rating mayor a 5.0 lanza ValueError
# un juego con rating menor a 0.0 lanza ValueError
# un juego con precio 0.0 y rating 0.0 es válido


# --------------------------------------------------------------------------
# GameStore — Catálogo
# --------------------------------------------------------------------------

# agregar un juego aumenta el tamaño del catálogo en 1


def test_should_add_a_game_to_the_catalog_and_increate_the_size_of_this_one() -> None:
    subject = game_store.GameStore()
    assert subject.catalog_size() == 0
    game_to_add = game_store.Game(
        title="Clair Obscur: Expedition 33", genre="RPG", price=39.99, rating=4.9
    )
    subject.add_to_catalog(game=game_to_add)
    assert subject.catalog_size() == 1


# agregar el mismo juego dos veces lanza ValueError
# get_game retorna el juego correcto por título
# get_game lanza GameNotFoundError si el título no existe
# list_by_genre retorna solo juegos del género solicitado
# list_by_genre retorna los juegos ordenados por rating descendente
# list_by_genre retorna lista vacía si no hay juegos del género
# search encuentra juegos cuyo título contiene el query
# search es case-insensitive
# search retorna lista vacía si no hay coincidencias


# --------------------------------------------------------------------------
# GameStore — Carrito
# --------------------------------------------------------------------------

# agregar un juego al carrito aumenta cart_item_count en 1
# agregar un juego que no está en el catálogo lanza GameNotFoundError
# agregar el mismo juego dos veces al carrito lanza GameAlreadyInCartError
# remove_from_cart reduce cart_item_count en 1
# remove_from_cart lanza GameNotInCartError si el juego no está en el carrito
# cart_total retorna la suma correcta de los precios
# cart_total retorna 0.0 si el carrito está vacío
# clear_cart deja el carrito vacío


# --------------------------------------------------------------------------
# GameStore — Descuentos
# --------------------------------------------------------------------------

# apply_coupon con código válido retorna el porcentaje correcto
# apply_coupon con código inválido lanza InvalidCouponError
# apply_coupon con un cupón ya usado lanza InvalidCouponError
# final_total sin cupón ni juegos con descuento de género es igual a cart_total
# final_total con cupón STEAM2025 aplica 10% sobre el total
# final_total descuenta 15% a los juegos RPG del carrito
# final_total descuenta 10% a los juegos Indie del carrito
# final_total nunca retorna un valor negativo


# ==========================================================================
# PARTE 2 — Refactoriza y vuelve a probar
# ==========================================================================
#
# Ahora que tienes los tests de la Parte 1 en verde, mira hacia atrás:
#
#   - ¿Cuántas líneas de setup necesitaste antes de poder probar
#     apply_coupon o final_total?
#   - ¿Qué pasa si cambias la lógica del catálogo? ¿Cuántos tests
#     de carrito o descuentos se rompen sin que hayas tocado esa lógica?
#
# Esas son las señales de que hay demasiadas responsabilidades juntas.
#
# ----------------------------------------------------------------------
# TU TAREA
# ----------------------------------------------------------------------
# 1. Crea tres módulos nuevos en src/:
#
#       src/catalog.py     → clase Catalog     con: add, get, list_by_genre, search
#       src/cart.py        → clase Cart        con: add, remove, total, count, clear
#       src/discounts.py   → clase Discounts   con: apply_coupon, by_genre, final_total
#
#    Mueve Game y las excepciones a src/models.py
#
# 2. Crea tests/test_catalog.py, tests/test_cart.py, tests/test_discounts.py
#
#    Verás que:
#       - test_catalog.py  no necesita carrito ni cupones para funcionar
#       - test_cart.py     recibe objetos Game directamente, sin catálogo
#       - test_discounts.py recibe una lista de Game, sin catálogo ni store
#
# 3. Compara el setup de cada test antes y después del refactor.
#    ¿Cuántas líneas de arrange necesita ahora cada test?
