import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self):
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_API_SECRET")
        self.origin = os.getenv("ORIGIN_IATA", "BLR")
        self.access_token = self._get_token()

    def _get_token(self):
        auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        response = requests.post(
            auth_url,
            data={
                "grant_type": "client_credentials",
                "client_id": self.api_key,
                "client_secret": self.api_secret
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        response.raise_for_status()
        return response.json()["access_token"]

    def get_destination_code(self, city_name):
        api_key = os.getenv("AVIATION_STACK_API_KEY")
        url = f"https://api.aviationstack.com/v1/cities?access_key={api_key}&city_name={city_name}"
        response = requests.get(url=url)
        response.raise_for_status()
        return response.json()["data"][0]["iata_code"]

    def get_price(self, iata_code, price_type):
        endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        params = {
            "originLocationCode": self.origin,
            "destinationLocationCode": iata_code,
            "departureDate": "2026-04-01",
            "adults": 1,
            "currencyCode": "INR"
        }
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(url=endpoint, params=params, headers=headers)
        response.raise_for_status()
        return response.json()["data"][0]["price"][price_type]

    def check_cheapest(self, iata_code):
        self.access_token = self._get_token()  # refresh token
        endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        cheapest = None

        for days_ahead in range(1, 180, 3):
            check_date = (datetime.today() + timedelta(days=days_ahead)).strftime("%Y-%m-%d")
            params = {
                "originLocationCode": self.origin,
                "destinationLocationCode": iata_code,
                "departureDate": check_date,
                "adults": 1,
                "currencyCode": "INR",
                "max": 1
            }
            response = requests.get(url=endpoint, params=params, headers=headers)
            if response.status_code != 200:
                continue
            data = response.json()
            if not data.get("data"):
                continue
            price = float(data["data"][0]["price"]["grandTotal"])
            if cheapest is None or price < cheapest["price"]:
                cheapest = {
                    "destination": iata_code,
                    "departure_date": check_date,
                    "price": price
                }

        if cheapest:
            print(f"✅ Cheapest to {iata_code} | {cheapest['departure_date']} | ₹{cheapest['price']}")
        else:
            print(f"❌ No flights found for {iata_code}")

        return cheapest["price"], cheapest["departure_date"]