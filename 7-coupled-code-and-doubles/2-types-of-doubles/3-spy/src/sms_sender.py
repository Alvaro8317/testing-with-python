class SmsSender:
    def send(self, phone: str, message: str) -> dict:
        print(f"[SMS] To: {phone} | Message: {message}")
        return {"status": "sent", "to": phone, "channel": "sms"}
