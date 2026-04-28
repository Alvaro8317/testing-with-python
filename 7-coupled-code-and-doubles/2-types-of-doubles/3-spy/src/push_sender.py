class PushSender:
    def send_push_notification_to_single_receiver(self, message: str, receiver_id: str) -> None:
        print(f"Sent push notification to {receiver_id} with message {message}")

    def send_push_notification_to_all_available_receivers(self, message: str) -> None:
        print(f"Send massive message to all receivers with message {message}")
