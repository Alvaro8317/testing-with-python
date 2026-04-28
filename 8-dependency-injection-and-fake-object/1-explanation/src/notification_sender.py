class NotificationSender:
    def send_message(self, message: str, user_id: str) -> dict[str, str]:
        print("Acá se realiza una implementación real de enviar notificaciones con SNS")
        return {"status": "sent", "user_id": user_id, "message": message}
