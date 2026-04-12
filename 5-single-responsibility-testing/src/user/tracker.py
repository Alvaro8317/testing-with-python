from datetime import datetime

from src.user import formatter, user


class ActivityTracker:
    ACTIVE_DAYS_THRESHOLD = 30

    def __init__(self, formatter: formatter.UserFormatter):
        self.formatter = formatter

    def is_active(self, user_to_track: user.User) -> bool:
        """
        Determina si el usuario está activo.

        Un usuario está activo si se logueó en los últimos
        ACTIVE_DAYS_THRESHOLD días.
        """
        if user_to_track.last_login is None:
            return False
        days_since_login = (datetime.now() - user_to_track.last_login).days
        return days_since_login <= self.ACTIVE_DAYS_THRESHOLD

    def activity_summary(self, user_to_track: user.User) -> dict:
        """
        Genera un resumen de la actividad del usuario.

        Retorna un diccionario con las métricas más relevantes
        para reportes y dashboards de administración.
        """
        return {
            "user": self.formatter.display_name(user_to_track),
            "plan": self.formatter.plan_label(user_to_track),
            "login_count": user_to_track.login_count,
            "last_login": user_to_track.last_login.isoformat()
            if user_to_track.last_login
            else "Never",
            "is_active": self.is_active(user_to_track),
            "account_age_days": (datetime.now() - user_to_track.created_at).days,
        }
