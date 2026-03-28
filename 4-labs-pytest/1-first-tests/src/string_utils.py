def reverse_words(sentence: str) -> str:
    """
    Invierte el orden de las palabras en una oración.

    Ejemplos:
        reverse_words("hola mundo")   -> "mundo hola"
        reverse_words("uno dos tres") -> "tres dos uno"
        reverse_words("solo")         -> "solo"
        reverse_words("")             -> ""
    """
    if not sentence:
        return ""
    words = sentence.split()
    return " ".join(reversed(words))


def is_palindrome(text: str) -> bool:
    """
    Determina si una cadena es un palíndromo ignorando mayúsculas y espacios.

    Ejemplos:
        is_palindrome("radar")        -> True
        is_palindrome("Anita")        -> False
        is_palindrome("A man a plan") -> False   # espacios cuentan
        is_palindrome("")             -> True
    """
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_vowels(text: str) -> int:
    """
    Cuenta las vocales (a, e, i, o, u) en una cadena, ignorando mayúsculas.

    Ejemplos:
        count_vowels("hola")     -> 2
        count_vowels("PYTHON")   -> 1
        count_vowels("rhythm")   -> 0
        count_vowels("")         -> 0
    """
    return sum(1 for ch in text.lower() if ch in "aeiou")


def capitalize_words(text: str) -> str:
    """
    Pone en mayúscula la primera letra de cada palabra, el resto en minúscula.

    Ejemplos:
        capitalize_words("hola mundo")    -> "Hola Mundo"
        capitalize_words("PYTHON ES FUN") -> "Python Es Fun"
        capitalize_words("")              -> ""
    """
    if not text:
        return ""
    return " ".join(word.capitalize() for word in text.split())


def truncate(text: str, max_length: int) -> str:
    """
    Recorta el texto a max_length caracteres. Si fue recortado, agrega '...'.

    Ejemplos:
        truncate("Hola mundo", 4)  -> "Hola..."
        truncate("Hola", 10)       -> "Hola"
        truncate("Hola", 4)        -> "Hola"
        truncate("", 5)            -> ""
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."