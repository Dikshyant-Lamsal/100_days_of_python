import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        self.sheety_base = os.getenv("SHEETY_ENDPOINT")

    def flight_data(self):
        response = requests.get(url=self.sheety_base)
        response.raise_for_status()
        return response.json()

    def update_flight_data(self, row, iata_code):
        url = f"{self.sheety_base}/{row}"
        body = {"sheet1": {"iataCode": iata_code}}
        response = requests.put(url=url, json=body)
        response.raise_for_status()

    def set_initial_price(self, row, price):
        url = f"{self.sheety_base}/{row}"
        body = {"sheet1": {"lowestPrice": price}}
        response = requests.put(url=url, json=body)
        response.raise_for_status()

    def update_price_date(self, row, iata_code, price, date):
        url = f"{self.sheety_base}/{row}"
        body = {
            "sheet1": {
                "iataCode": iata_code,
                "lowestPrice": price,
                "cheapestDate": date
            }
        }
        response = requests.put(url=url, json=body)
        response.raise_for_status()