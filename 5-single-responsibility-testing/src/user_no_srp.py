"""
Clase User con múltiples responsabilidades.

Esta clase viola el principio de Single Responsibility porque:
    1. Gestiona los datos del usuario
    2. Formatea y valida información del usuario
    3. Genera el contenido de notificaciones
    4. Calcula métricas del usuario

Todo esto en una sola clase — sin dependencias externas,
por lo que aún es posible testearlo, pero con un costo creciente
en complejidad, setup y claridad de los tests.
"""

import re
from datetime import datetime


class User:
    """
    Clase de usuario con demasiadas responsabilidades.

    A primera vista parece razonable — es solo una clase de usuario.
    Pero a medida que el negocio crece, cada nueva feature
    del sistema aterriza aquí porque "es algo relacionado con el usuario".

    El resultado es una clase que crece sin freno y que
    mezcla responsabilidades que no tienen nada que ver entre sí.
    """

    VALID_PLANS = ("free", "pro", "enterprise")
    MIN_PASSWORD_LENGTH = 8
    EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        plan: str = "free",
    ):
        # Responsabilidad 1: datos del usuario
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.plan = plan
        self.created_at = datetime.now()
        self.last_login: datetime | None = None
        self.login_count: int = 0

    # ── Responsabilidad 1: datos y estado del usuario ─────────────────────────

    def register_login(self) -> None:
        """Registra un nuevo inicio de sesión del usuario."""
        self.last_login = datetime.now()
        self.login_count += 1

    def upgrade_plan(self, new_plan: str) -> None:
        """Actualiza el plan del usuario."""
        # Problema: la validación del plan vive aquí,
        # mezclada con la mutación de estado
        if new_plan not in self.VALID_PLANS:
            raise ValueError(f"Invalid plan: {new_plan}. Must be one of {self.VALID_PLANS}")
        self.plan = new_plan

    # ── Responsabilidad 2: validación ─────────────────────────────────────────

    def is_email_valid(self) -> bool:
        """Valida que el email tenga formato correcto."""
        return bool(self.EMAIL_PATTERN.match(self.email))

    def is_password_valid(self) -> bool:
        """Valida que la contraseña cumpla los requisitos mínimos."""
        return len(self.password) >= self.MIN_PASSWORD_LENGTH

    def is_valid(self) -> bool:
        """
        Valida que el usuario esté completo y sea válido.

        Problema: esta validación mezcla reglas de datos (email, password)
        con reglas de negocio (plan válido, nombre no vacío).
        Son responsabilidades diferentes aunque parezcan relacionadas.
        """
        if not self.first_name.strip():
            raise ValueError("First name cannot be empty")
        if not self.last_name.strip():
            raise ValueError("Last name cannot be empty")
        if not self.is_email_valid():
            raise ValueError(f"Invalid email format: {self.email}")
        if not self.is_password_valid():
            raise ValueError(f"Password must be at least {self.MIN_PASSWORD_LENGTH} characters")
        if self.plan not in self.VALID_PLANS:
            raise ValueError(f"Invalid plan: {self.plan}")
        return True

    # ── Responsabilidad 3: formateo y presentación ────────────────────────────

    def full_name(self) -> str:
        """Retorna el nombre completo formateado."""
        return f"{self.first_name.strip().title()} {self.last_name.strip().title()}"

    def display_name(self) -> str:
        """
        Retorna el nombre para mostrar en la interfaz.

        Problema: la lógica de presentación vive en el modelo de datos.
        Si el equipo de frontend quiere cambiar cómo se muestra el nombre,
        tiene que modificar la clase User.
        """
        return f"{self.full_name()} ({self.email})"

    def plan_label(self) -> str:
        """
        Retorna la etiqueta legible del plan actual.

        Problema: este mapeo de plan a etiqueta es lógica de presentación,
        no lógica de dominio del usuario.
        """
        labels = {
            "free": "Free Plan",
            "pro": "Pro Plan 🚀",
            "enterprise": "Enterprise Plan ⭐",
        }
        return labels.get(self.plan, "Unknown Plan")

    # ── Responsabilidad 4: generación de notificaciones ───────────────────────

    def welcome_email_subject(self) -> str:
        """
        Genera el asunto del email de bienvenida.

        Problema: el contenido de un email no tiene nada que ver
        con la representación de un usuario. Si marketing quiere
        cambiar el copy del email, tiene que tocar User.
        """
        return f"Welcome to the platform, {self.first_name}!"

    def welcome_email_body(self) -> str:
        """
        Genera el cuerpo del email de bienvenida.

        Problema: el mismo que welcome_email_subject.
        Además, este método conoce detalles de formato (saltos de línea,
        estructura del mensaje) que no corresponden a un modelo de datos.
        """
        return (
            f"Hi {self.full_name()},\n\n"
            f"Your account has been created successfully.\n"
            f"You are currently on the {self.plan_label()}.\n\n"
            f"If you have any questions, reply to this email.\n\n"
            f"The Team"
        )

    def plan_upgrade_email_subject(self) -> str:
        """Genera el asunto del email de actualización de plan."""
        return f"Your plan has been updated to {self.plan_label()}"

    def plan_upgrade_email_body(self) -> str:
        """Genera el cuerpo del email de actualización de plan."""
        return (
            f"Hi {self.full_name()},\n\n"
            f"Your plan has been successfully updated.\n"
            f"You now have access to all {self.plan_label()} features.\n\n"
            f"The Team"
        )

    # ── Responsabilidad 5: métricas y estado de actividad ────────────────────

    def is_active(self) -> bool:
        """
        Determina si el usuario está activo.

        Problema: la definición de "activo" es lógica de negocio
        que puede cambiar independientemente del modelo de usuario.
        Si el equipo decide que "activo" significa algo diferente,
        tienen que modificar User.
        """
        if self.last_login is None:
            return False
        days_since_login = (datetime.now() - self.last_login).days
        return days_since_login <= 30

    def activity_summary(self) -> dict:
        """
        Genera un resumen de la actividad del usuario.

        Problema: generar reportes o resúmenes es responsabilidad
        de una capa de reporting, no del modelo de usuario.
        Mezclar esto aquí hace que los tests de User
        tengan que verificar también el formato de los reportes.
        """
        return {
            "user": self.display_name(),
            "plan": self.plan_label(),
            "login_count": self.login_count,
            "last_login": self.last_login.isoformat() if self.last_login else "Never",
            "is_active": self.is_active(),
            "account_age_days": (datetime.now() - self.created_at).days,
        }

    def __repr__(self) -> str:
        return f"User(email={self.email!r}, plan={self.plan!r})"
