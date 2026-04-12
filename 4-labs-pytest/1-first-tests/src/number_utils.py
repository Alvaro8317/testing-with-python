def is_leap_year(year: int) -> bool:
    """
    Determina si un año es bisiesto.
    Un año es bisiesto si es divisible por 4,
    excepto los siglos, que deben ser divisibles por 400.

    Ejemplos:
        is_leap_year(2000) -> True
        is_leap_year(1900) -> False
        is_leap_year(2024) -> True
        is_leap_year(2023) -> False
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convierte una temperatura de Celsius a Fahrenheit.
    Fórmula: F = C * 9/5 + 32

    Ejemplos:
        celsius_to_fahrenheit(0)   -> 32.0
        celsius_to_fahrenheit(100) -> 212.0
        celsius_to_fahrenheit(-40) -> -40.0
    """
    return celsius * 9 / 5 + 32


def clamp(value: float, minimum: float, maximum: float) -> float:
    """
    Limita un valor dentro de un rango [minimum, maximum].

    Ejemplos:
        clamp(5, 0, 10)   -> 5
        clamp(-3, 0, 10)  -> 0
        clamp(15, 0, 10)  -> 10
        clamp(0, 0, 10)   -> 0
    """
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def fizzbuzz(n: int) -> str:
    """
    Retorna:
      - "FizzBuzz" si n es divisible por 3 y por 5
      - "Fizz"     si n es divisible solo por 3
      - "Buzz"     si n es divisible solo por 5
      - El número como string en cualquier otro caso

    Ejemplos:
        fizzbuzz(15) -> "FizzBuzz"
        fizzbuzz(9)  -> "Fizz"
        fizzbuzz(10) -> "Buzz"
        fizzbuzz(7)  -> "7"
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def percentage(part: float, total: float) -> float:
    """
    Calcula qué porcentaje representa `part` respecto a `total`.
    Lanza ValueError si total es 0.

    Ejemplos:
        percentage(25, 200) -> 12.5
        percentage(50, 50)  -> 100.0
        percentage(0, 100)  -> 0.0
    """
    if total == 0:
        raise ValueError("El total no puede ser 0")
    return (part / total) * 100
