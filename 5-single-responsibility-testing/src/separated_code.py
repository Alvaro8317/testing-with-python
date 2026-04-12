class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def complete_name(self) -> str:
        return self.name.strip().title()


class EmailService:
    def enviar_bienvenida(self, user: User) -> None:
        print(f"Enviando email de bienvenida a {user.email}")
