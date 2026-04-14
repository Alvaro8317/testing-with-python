from unittest import mock

import pytest
from src import email_sender, notification_service, sms_sender


@pytest.fixture
def fxt_email_sender_instance() -> email_sender.EmailSender:
    return email_sender.EmailSender()


@pytest.fixture
def fxt_sms_sender_instance() -> sms_sender.SmsSender:
    return sms_sender.SmsSender()


@pytest.fixture
def fxt_email_spy(fxt_email_sender_instance: email_sender.EmailSender) -> mock.MagicMock:
    spy = mock.MagicMock(wraps=fxt_email_sender_instance.send)
    fxt_email_sender_instance.send = spy
    return spy


@pytest.fixture
def fxt_sms_spy(fxt_sms_sender_instance: sms_sender.SmsSender) -> mock.MagicMock:
    spy = mock.MagicMock(wraps=fxt_sms_sender_instance.send)
    fxt_sms_sender_instance.send = spy
    return spy


@pytest.fixture
def fxt_subject(
    fxt_email_sender_instance: email_sender.EmailSender,
    fxt_sms_sender_instance: sms_sender.SmsSender,
) -> notification_service.NotificationService:
    return notification_service.NotificationService(
        email_sender=fxt_email_sender_instance,
        sms_sender=fxt_sms_sender_instance,
    )
