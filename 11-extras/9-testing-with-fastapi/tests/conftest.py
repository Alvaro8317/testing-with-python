from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from src import database, main


@pytest.fixture(autouse=True)
def fxt_reset_db() -> Generator[None, None, None]:
    database.reset()
    yield
    database.reset()


@pytest.fixture
def fxt_client() -> TestClient:
    return TestClient(main.app)


@pytest.fixture
def fxt_sample_cost() -> dict[str, str | float]:
    return {
        "description": "Internet bill",
        "amount": 50.0,
        "category": "Services",
        "date": "2026-05-01",
    }
