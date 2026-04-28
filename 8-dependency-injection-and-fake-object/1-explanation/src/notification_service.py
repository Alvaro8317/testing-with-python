from src import notification_sender


class NotificationService:
    def __init__(self, notification_sender: notification_sender.NotificationSender) -> None:
        self.sender = notification_sender

    def notify(self, user_id: str) -> dict[str, str]:
        return self.sender.send_message("Hello world", user_id)
