import re

from src.user import user

EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
MIN_PASSWORD_LENGTH = 8
VALID_PLANS = ("free", "pro", "enterprise")


class UserValidation:
    def validate_email(self, email: str) -> None:
        """Valida que el email tenga formato correcto, si no lo tiene, lanza ValueError."""
        if not bool(EMAIL_PATTERN.match(email)):
            raise ValueError(f"Invalid email format: {email}")

    def validate_password(self, password: str) -> None:
        """Valida que la contraseña cumpla los requisitos mínimos."""
        if not len(password) >= MIN_PASSWORD_LENGTH:
            raise ValueError(f"Password must be at least {MIN_PASSWORD_LENGTH} characters")

    def validate_plan(self, plan: str) -> None:
        if plan not in VALID_PLANS:
            raise ValueError(f"Invalid plan: {plan}")

    def is_valid(self, user: user.User) -> None:
        """
        Valida que el usuario esté completo y sea válido.

        Problema: esta validación mezcla reglas de datos (email, password)
        con reglas de negocio (plan válido, nombre no vacío).
        Son responsabilidades diferentes aunque parezcan relacionadas.
        """
        if not user.first_name.strip():
            raise ValueError("First name cannot be empty")
        if not user.last_name.strip():
            raise ValueError("Last name cannot be empty")
        self.validate_email(email=user.email)
        self.validate_password(password=user.password)
        self.validate_plan(plan=user.plan)
