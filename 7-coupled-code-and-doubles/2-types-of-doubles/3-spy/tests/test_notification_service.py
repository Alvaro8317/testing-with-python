from unittest import mock

import pytest
from src import notification_service


@pytest.mark.spy
def test_sends_email_notification_when_email_is_present(
    fxt_subject: notification_service.NotificationService,
    fxt_email_spy: mock.MagicMock,
    fxt_sms_spy: mock.MagicMock,
) -> None:
    user = {"email": "ana@test.com"}

    fxt_subject.notify_user(user=user, message="Bienvenida!")

    fxt_email_spy.assert_called_once_with(
        to="ana@test.com",
        subject="Notificación",
        body="Bienvenida!",
    )
    fxt_sms_spy.assert_not_called()


@pytest.mark.spy
def test_sends_sms_notification_when_phone_is_present(
    fxt_subject: notification_service.NotificationService,
    fxt_email_spy: mock.MagicMock,
    fxt_sms_spy: mock.MagicMock,
) -> None:
    user = {"phone": "+57300000000"}

    fxt_subject.notify_user(user, "Tu pedido llegó")

    fxt_sms_spy.assert_called_once_with(
        phone="+57300000000",
        message="Tu pedido llegó",
    )
    fxt_email_spy.assert_not_called()


@pytest.mark.spy
def test_sends_notifications_through_both_channels(
    fxt_subject: notification_service.NotificationService,
    fxt_email_spy: mock.MagicMock,
    fxt_sms_spy: mock.MagicMock,
) -> None:
    user = {"email": "carlos@test.com", "phone": "+57311111111"}

    fxt_subject.notify_user(user, "Alerta importante")

    assert fxt_email_spy.call_count == 1
    fxt_email_spy.assert_called_once_with(
        to="carlos@test.com",
        subject="Notificación",
        body="Alerta importante",
    )

    assert fxt_sms_spy.call_count == 1
    fxt_sms_spy.assert_called_once_with(
        phone="+57311111111",
        message="Alerta importante",
    )


@pytest.mark.spy
def test_does_not_send_notifications_when_no_channels_available(
    fxt_subject: notification_service.NotificationService,
    fxt_email_spy: mock.MagicMock,
    fxt_sms_spy: mock.MagicMock,
) -> None:
    user = {"name": "Fantasma"}

    results = fxt_subject.notify_user(user, "Hola?")

    fxt_email_spy.assert_not_called()
    fxt_sms_spy.assert_not_called()
    assert results == []


@pytest.mark.spy
def test_returns_actual_email_result(
    fxt_subject: notification_service.NotificationService,
) -> None:
    user = {"email": "sofia@test.com"}

    results = fxt_subject.notify_user(user, "Prueba")

    assert results[0]["status"] == "sent"
    assert results[0]["channel"] == "email"


@pytest.mark.spy
def test_call_order_when_both_channels_are_used(
    fxt_subject: notification_service.NotificationService,
    fxt_email_spy: mock.MagicMock,
    fxt_sms_spy: mock.MagicMock,
) -> None:
    user = {"email": "luis@test.com", "phone": "+57322222222"}

    fxt_subject.notify_user(user, "Mensaje")

    fxt_email_spy.assert_called_with(
        to="luis@test.com",
        subject="Notificación",
        body="Mensaje",
    )
    fxt_sms_spy.assert_called_with(
        phone="+57322222222",
        message="Mensaje",
    )


@pytest.mark.spy
def test_multiple_users_accumulate_calls(
    fxt_subject: notification_service.NotificationService,
    fxt_email_spy: mock.MagicMock,
) -> None:
    users = [
        {"email": "a@test.com"},
        {"email": "b@test.com"},
        {"email": "c@test.com"},
    ]

    for user in users:
        fxt_subject.notify_user(user, "Promo")

    assert fxt_email_spy.call_count == 3
    recipients = [call.kwargs["to"] for call in fxt_email_spy.call_args_list]
    assert recipients == ["a@test.com", "b@test.com", "c@test.com"]
