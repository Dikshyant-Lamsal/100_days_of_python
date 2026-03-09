from data_manager import DataManager

class FlightData:
    """This class is responsible for structuring the flight data."""

    def __init__(self):
        self.data_manager = DataManager()
        self.flight_data = self.data_manager.flight_data()
        self.cities = [city["city"] for city in self.flight_data["sheet1"]]
        self.city_codes = {city["city"]: city["iataCode"] for city in self.flight_data["sheet1"]}
        self.lowest_prices = {city["city"]: city["lowestPrice"] for city in self.flight_data["sheet1"]}
        self.cheapest_date = {city["city"]: city["cheapestDate"] for city in self.flight_data["sheet1"]}