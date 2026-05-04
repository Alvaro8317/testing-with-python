from src import notification_sender


class FakeNotificationSender(notification_sender.NotificationSender):
    def send_message(self, message: str, user_id: str) -> dict[str, str]:
        print(
            "Acá se realiza una implementación fake de enviar "
            "notificaciones con SNS, solo en memoria se hace"
        )
        return {"status": "sent", "user_id": user_id, "message": message}
