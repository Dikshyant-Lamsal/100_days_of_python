from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_data = FlightData()
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


def update_iata_codes():
    for city in flight_data.cities:
        if flight_data.city_codes[city] in ("", "TEST"):
            iata_code = flight_search.get_destination_code(city)
            data_manager.update_flight_data(
                row=flight_data.cities.index(city) + 2,
                iata_code=iata_code
            )


def update_base_price():
    for city in flight_data.cities:
        if not flight_data.lowest_prices[city]:
            iata_code = flight_data.city_codes[city]
            price = flight_search.get_price(iata_code=iata_code, price_type="base")
            data_manager.set_initial_price(
                row=flight_data.cities.index(city) + 2,
                price=price
            )


def consolidate_database():
    update_base_price()
    update_iata_codes()


def check_cheapest_price():
    for city in flight_data.cities:
        iata_code = flight_data.city_codes[city]
        stored_price = flight_data.lowest_prices[city]
        updated_price, updated_date = flight_search.check_cheapest(iata_code=iata_code)
        if stored_price > updated_price:
            data_manager.update_price_date(
                row=flight_data.cities.index(city) + 2,
                iata_code=iata_code,
                price=updated_price,
                date=updated_date
            )
            notification_manager.send_message(
                price=updated_price,
                date=updated_date,
                city=city
            )


check_cheapest_price()