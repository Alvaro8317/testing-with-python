import pytest
from src import user_account


@pytest.fixture
def fxt_user_account() -> user_account.UserAccount:
    return user_account.UserAccount(
        username="Alvaro8317", email="awesome_email@gmail.com", initial_balance=100.0
    )


def test_should_deposit_money(fxt_user_account: user_account.UserAccount) -> None:
    fxt_user_account.deposit(25.50)
    assert fxt_user_account.balance == 125.50
    assert not fxt_user_account.is_locked
    assert fxt_user_account.transaction_count() == 1
