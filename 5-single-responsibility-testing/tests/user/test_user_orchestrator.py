from src.user import user_orchestrator


def test_should_create_user_and_test_all_workflow() -> None:
    result = user_orchestrator.create_user_and_test_all_workflow(
        first_name="fake first name",
        last_name="fake last name",
        email="a-fake-email@email.com",
        password="super-fake-secret",
    )
    assert result.first_name == "fake first name"
