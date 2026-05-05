from typing import Any


def sum_numbers(x: int | float, y: int | float) -> int | float:
    return x + y


print(sum_numbers(1, 2))


def calculate_complete_name(first_name: str, last_name: str) -> str:
    return f"{first_name} - {last_name}"


complete_name = calculate_complete_name(first_name="Alvaro", last_name="Garzón")
print(complete_name)

print(sum_numbers(1.15, 2.23))
print(sum_numbers(1.15, 2.23))

my_variable: str = "Hola"
my_variable_int: int = 1
my_variable_float: float | None = None
my_variable_float = 10.3
my_variable_bool: bool = True
my_list_typed: list[str | int] = ["a", "b", "c"]
my_list_typed.append("1")
my_list_typed.append(1)

my_dict_typed: dict[str, str | int] = {"first_name": "Alvaro", "age": 28}


def _log_everything_is_ok(message: Any) -> None:
    print(f"Everything is ok, message: {message}")


_log_everything_is_ok(message="Hi there! ")
_log_everything_is_ok(message=2)
_log_everything_is_ok(message=[2, 3, 4, 5])
_log_everything_is_ok(message={1, 2, 3})
