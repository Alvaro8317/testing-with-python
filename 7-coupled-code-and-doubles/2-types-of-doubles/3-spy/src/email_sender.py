class EmailSender:
    def send(self, to: str, subject: str, body: str) -> dict:
        # En producción aquí iría el cliente SMTP real
        print(f"[EMAIL] To: {to} | Subject: {subject}")
        return {"status": "sent", "to": to, "channel": "email"}
