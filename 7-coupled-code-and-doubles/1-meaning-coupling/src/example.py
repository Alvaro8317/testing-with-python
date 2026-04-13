class Class1:
    x = True


class Class2:
    def my_method(self, valor: str) -> None:
        if Class1.x:  # If True
            self.value = valor


# my_class = Class2()
# my_class.my_method("Hola")
# print(my_class.value)

# Class1.x = False  # Cambio en clase 1, de la cuál está fuertemente acoplada la clase 2

# # Otro proceso
# my_class.my_method("Hola de nuevo")
# print(my_class.value)  # Debería de ser "hola de nuevo"
