import requests
import datetime
import geocoder
from dotenv import load_dotenv
import os

load_dotenv()

lat = geocoder.ip('me').latlng[0]
lon = geocoder.ip('me').latlng[1]

api_key = {os.getenv("api_key")}
open_weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=open_weather_params)
response.raise_for_status()
data = response.json()
data_list = data["list"]


def will_rain():
    for hour in data_list:
        weather_id = hour["weather"][0]["id"]
        if weather_id < 700:
            return True
    return False

if will_rain():
    print("Bring an umbrella.")
else:
    print("No rain today for the next 12 hours!")