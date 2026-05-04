import datetime

import pytest
from fastapi import testclient


@pytest.mark.fastapi
class TestCreateCost:
    def test_creates_cost_and_returns_201(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        response = fxt_client.post("/costs/", json=fxt_sample_cost)
        assert response.status_code == 201
        body: dict[str, object] = response.json()
        assert body["id"] == 1
        assert body["description"] == fxt_sample_cost["description"]
        assert body["amount"] == fxt_sample_cost["amount"]
        assert body["category"] == fxt_sample_cost["category"]

    def test_ids_auto_increment(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        first: dict[str, object] = fxt_client.post("/costs/", json=fxt_sample_cost).json()
        second: dict[str, object] = fxt_client.post("/costs/", json=fxt_sample_cost).json()
        assert second["id"] == first["id"] + 1  # type: ignore[operator]

    def test_returns_422_when_amount_is_zero(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        fxt_sample_cost["amount"] = 0
        response = fxt_client.post("/costs/", json=fxt_sample_cost)
        assert response.status_code == 422

    def test_returns_422_when_amount_is_negative(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        fxt_sample_cost["amount"] = -10
        response = fxt_client.post("/costs/", json=fxt_sample_cost)
        assert response.status_code == 422

    def test_returns_422_when_description_is_empty(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        fxt_sample_cost["description"] = ""
        response = fxt_client.post("/costs/", json=fxt_sample_cost)
        assert response.status_code == 422

    def test_uses_today_as_default_date(self, fxt_client: testclient.TestClient) -> None:
        payload: dict[str, str | float] = {
            "description": "Coffee",
            "amount": 3.5,
            "category": "Food",
        }
        response = fxt_client.post("/costs/", json=payload)
        assert response.status_code == 201
        assert response.json()["date"] == str(datetime.date.today())


@pytest.mark.fastapi
class TestListCosts:
    def test_returns_empty_list_initially(self, fxt_client: testclient.TestClient) -> None:
        response = fxt_client.get("/costs/")
        assert response.status_code == 200
        assert response.json() == []

    def test_returns_all_created_costs(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        fxt_client.post("/costs/", json=fxt_sample_cost)
        fxt_client.post("/costs/", json=fxt_sample_cost)
        response = fxt_client.get("/costs/")
        assert response.status_code == 200
        assert len(response.json()) == 2


@pytest.mark.fastapi
class TestGetCost:
    def test_returns_cost_by_id(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        created: dict[str, object] = fxt_client.post("/costs/", json=fxt_sample_cost).json()
        response = fxt_client.get(f"/costs/{created['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == created["id"]

    def test_returns_404_for_unknown_id(self, fxt_client: testclient.TestClient) -> None:
        response = fxt_client.get("/costs/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Cost not found"


@pytest.mark.fastapi
class TestUpdateCost:
    def test_updates_amount(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        created: dict[str, object] = fxt_client.post("/costs/", json=fxt_sample_cost).json()
        response = fxt_client.put(f"/costs/{created['id']}", json={"amount": 99.9})
        assert response.status_code == 200
        assert response.json()["amount"] == 99.9

    def test_partial_update_keeps_other_fields(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        created: dict[str, object] = fxt_client.post("/costs/", json=fxt_sample_cost).json()
        fxt_client.put(f"/costs/{created['id']}", json={"amount": 75.0})
        body: dict[str, object] = fxt_client.get(f"/costs/{created['id']}").json()
        assert body["description"] == fxt_sample_cost["description"]
        assert body["category"] == fxt_sample_cost["category"]
        assert body["amount"] == 75.0

    def test_returns_404_when_updating_unknown_id(self, fxt_client: testclient.TestClient) -> None:
        response = fxt_client.put("/costs/999", json={"amount": 10.0})
        assert response.status_code == 404

    def test_returns_422_when_updating_with_invalid_amount(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        created: dict[str, object] = fxt_client.post("/costs/", json=fxt_sample_cost).json()
        response = fxt_client.put(f"/costs/{created['id']}", json={"amount": -5})
        assert response.status_code == 422


@pytest.mark.fastapi
class TestDeleteCost:
    def test_deletes_existing_cost(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        created: dict[str, object] = fxt_client.post("/costs/", json=fxt_sample_cost).json()
        response = fxt_client.delete(f"/costs/{created['id']}")
        assert response.status_code == 204

    def test_cost_no_longer_accessible_after_deletion(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        created: dict[str, object] = fxt_client.post("/costs/", json=fxt_sample_cost).json()
        fxt_client.delete(f"/costs/{created['id']}")
        response = fxt_client.get(f"/costs/{created['id']}")
        assert response.status_code == 404

    def test_returns_404_when_deleting_unknown_id(self, fxt_client: testclient.TestClient) -> None:
        response = fxt_client.delete("/costs/999")
        assert response.status_code == 404

    def test_list_shrinks_after_deletion(
        self, fxt_client: testclient.TestClient, fxt_sample_cost: dict[str, str | float]
    ) -> None:
        c1: dict[str, object] = fxt_client.post("/costs/", json=fxt_sample_cost).json()
        fxt_client.post("/costs/", json=fxt_sample_cost)
        fxt_client.delete(f"/costs/{c1['id']}")
        assert len(fxt_client.get("/costs/").json()) == 1
