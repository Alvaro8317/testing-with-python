import pytest
import requests
from src import spiderman_client


class FakeResponse:
    def raise_for_status(self) -> None:
        pass

    def json(self) -> dict:
        return {"data": 123}


def fake_get(url: str) -> FakeResponse:
    return FakeResponse()


def test_should_get_character(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(requests, "get", fake_get)
    result = spiderman_client.get_character(123456)
    assert result.get("data") == 123
