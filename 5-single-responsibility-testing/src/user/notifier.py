from src.user import formatter, user


class UserNotifier:
    def __init__(self, user_formatter: formatter.UserFormatter) -> None:
        self.user_formatter = user_formatter

    def welcome_email_subject(self, user_to_notify: user.User) -> str:
        """
        Genera el asunto del email de bienvenida.

        Problema: el contenido de un email no tiene nada que ver
        con la representación de un usuario. Si marketing quiere
        cambiar el copy del email, tiene que tocar User.
        """
        return f"Welcome to the platform, {user_to_notify.first_name}!"

    def welcome_email_body(self, user_to_notify: user.User) -> str:
        """
        Genera el cuerpo del email de bienvenida.

        Problema: el mismo que welcome_email_subject.
        Además, este método conoce detalles de formato (saltos de línea,
        estructura del mensaje) que no corresponden a un modelo de datos.
        """
        return (
            f"Hi {self.user_formatter.full_name(user_to_format=user_to_notify)},\n\n"
            f"Your account has been created successfully.\n"
            "You are currently on the "
            f"{self.user_formatter.plan_label(user_to_format=user_to_notify)}.\n\n"
            f"If you have any questions, reply to this email.\n\n"
            f"The Team"
        )

    def plan_upgrade_email_subject(self, user_to_notify: user.User) -> str:
        """Genera el asunto del email de actualización de plan."""
        return (
            "Your plan has been updated to "
            f"{self.user_formatter.plan_label(user_to_format=user_to_notify)}"
        )

    def plan_upgrade_email_body(self, user_to_notify: user.User) -> str:
        """Genera el cuerpo del email de actualización de plan."""
        return (
            f"Hi {self.user_formatter.full_name(user_to_format=user_to_notify)},\n\n"
            f"Your plan has been successfully updated.\n"
            f"You now have access to all "
            f"{self.user_formatter.plan_label(user_to_format=user_to_notify)} features.\n\n"
            f"The Team"
        )
