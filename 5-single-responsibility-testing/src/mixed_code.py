class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def complete_name(self) -> str:
        return self.name.strip().title()

    def send_welcome_email(self) -> None:
        print(f"Enviando email de bienvenida a {self.email}")
