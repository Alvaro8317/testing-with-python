from src import example


def test_should_invoke_my_method() -> None:
    my_class = example.Class2()
    my_class.my_method("Hola")
    assert my_class.value == "Hola"


def test_should_invoke_my_method_modifying_class_1() -> None:
    my_class = example.Class2()
    example.Class1.x = False
    my_class.my_method("Hola")
    assert my_class.value == "Hola"
