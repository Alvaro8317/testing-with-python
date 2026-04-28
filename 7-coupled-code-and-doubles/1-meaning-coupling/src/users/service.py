from src.users import db


class UserService:
    """
    Servicio de usuarios con acoplamiento fuerte a la base de datos.

    El problema está en el __init__:
    UserService instancia DatabaseConnection directamente.
    No hay forma de reemplazarla desde afuera.
    """

    def __init__(self) -> None:
        # Acoplamiento fuerte — instancia la dependencia directamente
        # Para testear UserService, DatabaseConnection también se ejecuta
        # lo que significa que necesitas una base de datos real disponible
        self.db_connection = db.DatabaseConnection()
        # self.email_sender = SMTPClient()  # ← acoplamiento fuerte
        # self.report_gen = FileWriter()      # ← acoplamiento fuerte

    def register(self, name: str, email: str) -> dict:
        existing = self.db_connection.find_by_email(email)
        if existing:
            raise ValueError(f"Email already registered: {email}")

        user = {"name": name, "email": email}
        self.db_connection.save(user)
        return user

    def find_user(self, email: str) -> dict:
        user = self.db_connection.find_by_email(email)
        if not user:
            raise KeyError(f"User not found: {email}")
        return user
