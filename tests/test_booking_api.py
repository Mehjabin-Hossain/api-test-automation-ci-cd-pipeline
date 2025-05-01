import pytest
from utils.api_client import ApiClient
from utils.payloads import create_booking_payload


@pytest.fixture(scope="module")
def client():
    return ApiClient()


@pytest.fixture(scope="module")
def auth_token(client):
    response = client.authenticate()
    assert response.status_code == 200
    token = response.json().get("token")
    assert token, "Authentication token should be returned"
    return token


def test_get_booking_ids_returns_list(client):
    response = client.get_booking_ids()

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_booking_returns_booking_id(client):
    payload = create_booking_payload()
    response = client.create_booking(payload)

    assert response.status_code == 200
    data = response.json()
    assert "bookingid" in data
    assert data["bookingid"] > 0
    assert data["booking"] == payload


def test_get_booking_by_id_returns_same_booking(client):
    payload = create_booking_payload()
    create_response = client.create_booking(payload)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    get_response = client.get_booking(booking_id)
    assert get_response.status_code == 200
    assert get_response.json()["firstname"] == payload["firstname"]
    assert get_response.json()["lastname"] == payload["lastname"]


def test_update_booking_changes_booking_data(client, auth_token):
    payload = create_booking_payload()
    create_response = client.create_booking(payload)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    updated_payload = payload.copy()
    updated_payload["firstname"] = "Updated"
    updated_payload["lastname"] = "Client"

    update_response = client.update_booking(booking_id, updated_payload, auth_token)
    assert update_response.status_code == 200
    assert update_response.json()["firstname"] == updated_payload["firstname"]
    assert update_response.json()["lastname"] == updated_payload["lastname"]


def test_delete_booking_removes_booking(client, auth_token):
    payload = create_booking_payload()
    create_response = client.create_booking(payload)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    delete_response = client.delete_booking(booking_id, auth_token)
    assert delete_response.status_code == 201

    get_response = client.get_booking(booking_id)
    assert get_response.status_code in (403, 404)
