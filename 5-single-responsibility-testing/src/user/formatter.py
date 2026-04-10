from src.user import user

LABELS = {
    "free": "Free Plan",
    "pro": "Pro Plan 🚀",
    "enterprise": "Enterprise Plan ⭐",
}


class UserFormatter:
    def full_name(self, user_to_format: user.User) -> str:
        """Retorna el nombre completo formateado."""
        return (
            f"{user_to_format.first_name.strip().title()} "
            f"{user_to_format.last_name.strip().title()}"
        )

    def display_name(self, user_to_format: user.User) -> str:
        """
        Retorna el nombre para mostrar en la interfaz.

        Problema: la lógica de presentación vive en el modelo de datos.
        Si el equipo de frontend quiere cambiar cómo se muestra el nombre,
        tiene que modificar la clase User.
        """
        return f"{self.full_name(user_to_format=user_to_format)} ({user_to_format.email})"

    def plan_label(self, user_to_format: user.User) -> str:
        """
        Retorna la etiqueta legible del plan actual.

        Problema: este mapeo de plan a etiqueta es lógica de presentación,
        no lógica de dominio del usuario.
        """
        return LABELS.get(user_to_format.plan, "Unknown Plan")
