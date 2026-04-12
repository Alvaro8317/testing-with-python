import pytest
from src.user import user


@pytest.fixture
def fxt_user() -> user.User:
    return user.User(
        first_name="fake", last_name="name", email="fake@email.com", password="very-secret"
    )
