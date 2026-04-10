from src.user import formatter, notifier, tracker, user, validation


def create_user_and_test_all_workflow(
    first_name: str, last_name: str, email: str, password: str
) -> user.User:
    user_to_check = user.User(
        first_name=first_name, last_name=last_name, email=email, password=password
    )
    user_validator = validation.UserValidation()
    user_validator.is_valid(user=user_to_check)

    user_to_check.register_login()
    user_to_check.upgrade_plan(new_plan="pro")

    user_formatter = formatter.UserFormatter()
    user_notifier = notifier.UserNotifier(user_formatter=user_formatter)

    print(user_notifier.welcome_email_subject(user_to_notify=user_to_check))
    print(user_notifier.welcome_email_body(user_to_notify=user_to_check))
    print(user_notifier.plan_upgrade_email_subject(user_to_notify=user_to_check))
    print(user_notifier.plan_upgrade_email_body(user_to_notify=user_to_check))

    user_tracker = tracker.ActivityTracker(formatter=user_formatter)
    print(user_tracker.is_active(user_to_track=user_to_check))
    print(user_tracker.activity_summary(user_to_track=user_to_check))

    return user_to_check
