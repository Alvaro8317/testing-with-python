from unittest import mock

import pytest
from src import notification_service, push_sender


@pytest.fixture
def fxt_push_sender() -> mock.MagicMock:
    instance_push_sender = push_sender.PushSender()
    spy_push = mock.MagicMock(wraps=instance_push_sender)
    return spy_push


def test_notify_by_push_all_available(
    fxt_subject: notification_service.NotificationService, fxt_push_sender: mock.MagicMock
) -> None:
    fxt_subject.notify_by_push_all_available(push_sender=fxt_push_sender, message="Hola mundo")
    fxt_push_sender.send_push_notification_to_all_available_receivers.assert_called_once_with(
        message="Hola mundo"
    )
