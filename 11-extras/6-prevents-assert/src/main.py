def dividir(x: int, y: int) -> float:
    assert y != 0, "Error: no se puede dividir entre cero"
    return x / y


def create_user(name: str, email: str, age: int) -> bool:
    if "@" not in email:
        raise ValueError("Email invalido")
    if age < 18:
        raise ValueError("Invalid age, you must be over 18")
    return True


if __name__ == "__main__":
    create_user(name="Alvaro", email="exampleexample.com", age=12)
    # try:
    #     result = dividir(x=10, y=0)
    #     print(result)
    # except AssertionError as e:
    #     print("Error controlado exitosamente", e)
