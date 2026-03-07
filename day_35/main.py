import requests
import datetime
import geocoder
from dotenv import load_dotenv
import os
from twilio.rest import Client

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
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    sender_no = os.getenv("TWILIO_PHONE_NUMBER")
    receiver_no = os.getenv("RECEIVER_PHONE_NUMBER")
    message = client.messages.create(
        from_=sender_no,
        to=receiver_no,
        body="It will rain today within the next 12 hours. Don't forget to bring an umbrella!",
        )   
    print(message)
else:
    print("No rain today for the next 12 hours!")





