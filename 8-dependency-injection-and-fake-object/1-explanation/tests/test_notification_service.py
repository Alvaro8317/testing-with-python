from src import notification_service
from tests import fakes


def test_should_notify() -> None:
    service = notification_service.NotificationService(
        notification_sender=fakes.FakeNotificationSender()
    )
    result = service.notify("123")
    assert result == {"status": "sent", "user_id": "123", "message": "Hello world"}
