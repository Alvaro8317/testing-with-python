import dataclasses
from datetime import datetime


@dataclasses.dataclass(frozen=True)
class Person:
    name: str
    last_name: str
    age: int
    birthdate: datetime
    last_time_that_ate: datetime
    has_son_or_daughter: bool
    is_investor: bool
    money_that_has: int | float
    profession: str

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


alvaro_person = Person(
    name="Alvaro",
    last_name="Garzón",
    age=19,
    birthdate=datetime.now(),
    last_time_that_ate=datetime.now(),
    has_son_or_daughter=False,
    is_investor=True,
    money_that_has=1_000_000,
    profession="Softare engineer",
)
alvaro_person.walk()
alvaro_person.eat()
alvaro_person.make_a_greeting()

diana_person = Person(
    name="Diana",
    last_name="Fulanita",
    age=19,
    birthdate=datetime.now(),
    last_time_that_ate=datetime.now(),
    has_son_or_daughter=False,
    is_investor=True,
    money_that_has=1_000_000,
    profession="Softare engineer",
)
diana_person.walk()
diana_person.eat()
Person.make_a_greeting()
Person.sum_numbers(x=10, y=20)
