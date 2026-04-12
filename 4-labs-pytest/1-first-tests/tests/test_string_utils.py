from src import string_utils


def test_should_reverse_words_hi_world() -> None:
    result = string_utils.reverse_words("hola mundo")
    assert result == "mundo hola"


def test_should_validate_if_it_is_palindrome_radar() -> None:
    result = string_utils.is_palindrome("radar")
    assert result


def test_should_count_vowels() -> None:
    assert string_utils.count_vowels("hola") == 2


def test_should_capitalize_words() -> None:
    assert string_utils.capitalize_words("hola mundo") == "Hola Mundo"


def test_should_truncate_words() -> None:
    assert string_utils.truncate("Hola mundo", 4) == "Hola..."
