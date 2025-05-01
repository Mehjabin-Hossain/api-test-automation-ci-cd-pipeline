import requests
from utils import config


class ApiClient:
    def __init__(self):
        self.base_url = config.BASE_URL
        self.booking_endpoint = config.BOOKING_ENDPOINT
        self.ping_endpoint = config.PING_ENDPOINT
        self.auth_endpoint = config.AUTH_ENDPOINT
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def health_check(self):
        return self.session.get(self.ping_endpoint)

    def get_booking_ids(self, params=None):
        return self.session.get(self.booking_endpoint, params=params)

    def create_booking(self, payload):
        return self.session.post(self.booking_endpoint, json=payload)

    def get_booking(self, booking_id):
        return self.session.get(f"{self.booking_endpoint}/{booking_id}")

    def update_booking(self, booking_id, payload, token):
        headers = {"Cookie": f"token={token}", "Accept": "application/json"}
        return self.session.put(f"{self.booking_endpoint}/{booking_id}", json=payload, headers=headers)

    def delete_booking(self, booking_id, token):
        headers = {"Cookie": f"token={token}"}
        return self.session.delete(f"{self.booking_endpoint}/{booking_id}", headers=headers)

    def authenticate(self):
        response = self.session.post(self.auth_endpoint, json=config.TEST_USER)
        return response
