class Person:
    def __init__(self, name: str, last_name: str) -> None:
        self.name = name
        self.last_name = last_name

    @property
    def complete_name(self) -> str:
        return f"{self.name} {self.last_name}"

    def walk(self) -> None:
        print(f"Hi there, I'm {self.complete_name}, I'm walking just right now")

    def eat(self) -> None:
        print(f"Hi there, I'm {self.complete_name}, I'm eating just right now")

    @classmethod
    def make_a_greeting(cls) -> None:
        print("Hi there")

    @staticmethod
    def sum_numbers(x: int | float, y: int | float) -> None:
        print(x + y)


alvaro_person = Person(name="Alvaro", last_name="Garzón")
alvaro_person.walk()
alvaro_person.eat()
alvaro_person.make_a_greeting()

diana_person = Person(name="Diana", last_name="Fulanita")
diana_person.walk()
diana_person.eat()

Person.make_a_greeting()
Person.sum_numbers(x=10, y=20)
