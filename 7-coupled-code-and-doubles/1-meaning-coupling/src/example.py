class Clase1:
    x = True
    pass


class Clase2:
    def mi_metodo(self, valor: str) -> None:
        if Clase1.x:  # If True
            self.valor = valor


mi_clase = Clase2()
mi_clase.mi_metodo("Hola")
print(mi_clase.valor)

Clase1.x = False  # Cambio en clase 1, de la cuál está fuertemente acoplada la clase 2

# Otro proceso
mi_clase.mi_metodo("Hola de nuevo")
print(mi_clase.valor)  # Should be "hola de nuevo"
