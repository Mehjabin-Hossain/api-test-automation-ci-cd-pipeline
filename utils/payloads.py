import datetime


def create_booking_payload():
    today = datetime.date.today()
    return {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": today.isoformat(),
            "checkout": (today + datetime.timedelta(days=5)).isoformat()
        },
        "additionalneeds": "Breakfast"
    }
