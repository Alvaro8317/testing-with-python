def remove_duplicates(items: list) -> list:
    """
    Elimina duplicados conservando el orden de primera aparición.

    Ejemplos:
        remove_duplicates([1, 2, 2, 3, 1]) -> [1, 2, 3]
        remove_duplicates([])              -> []
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten(nested: list[list]) -> list:
    """
    Aplana una lista de listas un solo nivel.

    Ejemplos:
        flatten([[1, 2], [3, 4]])   -> [1, 2, 3, 4]
        flatten([[], [1], []])      -> [1]
        flatten([])                 -> []
    """
    result = []
    for sublist in nested:
        result.extend(sublist)
    return result


def chunk(items: list, size: int) -> list[list]:
    """
    Divide una lista en sublistas de tamaño size.
    El último grupo puede ser más pequeño.

    Lanza ValueError si size < 1.

    Ejemplos:
        chunk([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]
        chunk([], 3)          -> []
    """
    if size < 1:
        raise ValueError("size debe ser al menos 1")
    return [items[i : i + size] for i in range(0, len(items), size)]


def interleave(list_a: list, list_b: list) -> list:
    """
    Intercala los elementos de dos listas elemento a elemento.
    Si una lista es más larga, los elementos sobrantes se agregan al final.

    Ejemplos:
        interleave([1,3,5], [2,4,6]) -> [1,2,3,4,5,6]
        interleave([1,2],   [3])     -> [1,3,2]
        interleave([],      [1,2])   -> [1,2]
    """
    result = []
    for a, b in zip(list_a, list_b, strict=True):
        result.extend([a, b])
    longer = list_a[len(list_b) :] or list_b[len(list_a) :]
    result.extend(longer)
    return result


def top_n(items: list[int | float], n: int) -> list[int | float]:
    """
    Retorna los n elementos más grandes de la lista, ordenados de mayor a menor.
    Si n >= len(items) retorna todos los elementos ordenados.

    Lanza ValueError si n < 1.
    Lanza ValueError si la lista está vacía.

    Ejemplos:
        top_n([3,1,4,1,5], 3) -> [5, 4, 3]
        top_n([7,2],        5) -> [7, 2]
    """
    if n < 1:
        raise ValueError("n debe ser al menos 1")
    if not items:
        raise ValueError("La lista no puede estar vacía")
    return sorted(items, reverse=True)[:n]
