from src.user import formatter, notifier, user


def test_should_give_welcome_email_subject(fxt_user: user.User) -> None:
    user_formatter = formatter.UserFormatter()
    user_notifier = notifier.UserNotifier(user_formatter=user_formatter)
    result = user_notifier.welcome_email_subject(user_to_notify=fxt_user)
    assert result == f"Welcome to the platform, {fxt_user.first_name}!"
