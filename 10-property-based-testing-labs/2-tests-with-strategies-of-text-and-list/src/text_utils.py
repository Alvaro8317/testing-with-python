def slugify(text: str) -> str:
    """
    Convierte un título en un slug URL-friendly.
    - Convierte a minúsculas
    - Reemplaza espacios por guiones
    - Elimina caracteres que no sean letras, números o guiones

    Ejemplos:
        slugify("Hola Mundo")         -> "hola-mundo"
        slugify("  Python  Rules  ")  -> "python--rules"   <- espacios internos se convierten
        slugify("¡Título!")           -> "ttulo"            <- caracteres especiales eliminados
    """
    text = text.lower()
    text = text.replace(" ", "-")
    text = "".join(c for c in text if c.isalnum() or c == "-")
    return text


def word_count(text: str) -> int:
    """
    Cuenta las palabras de un texto separadas por espacios.
    Una cadena vacía o de solo espacios retorna 0.

    Ejemplos:
        word_count("hola mundo") -> 2
        word_count("  ")         -> 0
        word_count("")           -> 0
    """
    return len(text.split())


def truncate_to_summary(text: str, max_words: int) -> str:
    """
    Trunca el texto a max_words palabras.
    Si el texto fue truncado agrega '...' al final.
    Si max_words >= palabras totales retorna el texto sin modificar.

    Lanza ValueError si max_words < 1.

    Ejemplos:
        truncate_to_summary("uno dos tres", 2) -> "uno dos..."
        truncate_to_summary("uno dos tres", 5) -> "uno dos tres"
        truncate_to_summary("uno",          1) -> "uno"
    """
    if max_words < 1:
        raise ValueError("max_words debe ser al menos 1")
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + "..."


def normalize_whitespace(text: str) -> str:
    """
    Colapsa múltiples espacios consecutivos en uno solo y hace strip().

    Ejemplos:
        normalize_whitespace("hola   mundo")   -> "hola mundo"
        normalize_whitespace("  hola mundo  ") -> "hola mundo"
        normalize_whitespace("   ")            -> ""
    """
    return " ".join(text.split())


def capitalize_title(text: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.

    Ejemplos:
        capitalize_title("hola mundo")   -> "Hola Mundo"
        capitalize_title("PYTHON rules") -> "Python Rules"
    """
    return " ".join(word.capitalize() for word in text.split())
