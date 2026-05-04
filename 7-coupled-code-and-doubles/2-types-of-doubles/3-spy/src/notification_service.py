from src import email_sender, push_sender, sms_sender


class NotificationService:
    def __init__(
        self, email_sender: email_sender.EmailSender, sms_sender: sms_sender.SmsSender
    ) -> None:
        self.email_sender = email_sender
        self.sms_sender = sms_sender

    def notify_user(self, user: dict[str, str], message: str) -> list[dict]:
        """Notifica al usuario por todos sus canales disponibles."""
        results = []

        if email := user.get("email"):
            result = self.email_sender.send(
                to=email,
                subject="Notificación",
                body=message,
            )
            results.append(result)

        if phone := user.get("phone"):
            result = self.sms_sender.send(phone=phone, message=message)
            results.append(result)

        return results

    def notify_by_sms_only(self, email: str, message: str) -> list[dict[str, str]]:
        result = self.email_sender.send(to=email, subject="Welcome to this class", body=message)
        return [result]

    def notify_by_push_all_available(
        self, push_sender: push_sender.PushSender, message: str
    ) -> None:
        push_sender.send_push_notification_to_all_available_receivers(message=message)
