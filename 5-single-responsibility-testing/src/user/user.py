from datetime import datetime


class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        plan: str = "free",
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.plan = plan
        self.created_at = datetime.now()
        self.last_login: datetime | None = None
        self.login_count: int = 0

    def register_login(self) -> None:
        self.last_login = datetime.now()
        self.login_count += 1

    def upgrade_plan(self, new_plan: str) -> None:
        """Actualiza el plan del usuario."""
        self.plan = new_plan

    def __repr__(self) -> str:
        return f"User(email={self.email}, plan={self.plan})"
