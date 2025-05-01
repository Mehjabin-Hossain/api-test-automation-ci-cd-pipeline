from utils.api_client import ApiClient


def test_health_check_returns_201():
    client = ApiClient()

    response = client.health_check()

    assert response.status_code == 201
    assert response.text == "Created"
