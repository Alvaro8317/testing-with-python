import pytest
from src import validation


@pytest.mark.validations
def test_should_validate_email_with_gmail() -> None:
    assert validation.validate_email("user@gmail.com")


@pytest.mark.validations
def test_should_validate_email_with_business_email() -> None:
    assert validation.validate_email("user@company-email.com")


@pytest.mark.validations
def test_should_not_validate_email_because_does_not_have_at() -> None:
    assert not validation.validate_email("usercompany-email.com")


@pytest.mark.validations
def test_should_not_validate_email_because_is_empty() -> None:
    assert not validation.validate_email("")


@pytest.mark.validations
@pytest.mark.parametrize(
    "email, expected_result",
    [
        pytest.param("user@gmail.com", True, id="Case when email is gmail"),
        pytest.param("user@hotmail.com", True, id="Case when email is hotmail"),
        pytest.param("user@yahoo.com", True, id="Case when email is yahoo"),
        pytest.param("user@company-email.com", True, id="Case when is a company or business email"),
        pytest.param("user@aws.com", True, id="Case when email is aws"),
        pytest.param("user@google.com", True, id="Case when email is google"),
        pytest.param("usercompany-email.com", False, id="Case when does not have at in the email"),
        pytest.param("", False, id="Case when email is empty"),
        pytest.param(
            "alvaro|hotmail.com",
            True,
            id="Case when email has a pipe",
            marks=pytest.mark.xfail(reason="We do not support pipe yet"),
        ),
    ],
)
def test_should_validate_email(email: str, expected_result: bool) -> None:
    assert validation.validate_email(email=email) == expected_result
