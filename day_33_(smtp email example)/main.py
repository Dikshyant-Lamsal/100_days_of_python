import requests
import geocoder
from datetime import datetime
import smtplib
import time

MY_EMAIL = "diksclaude1@gmail.com"
MY_PASSWORD = ""
with open(".env") as file:
    for line in file:
        key, value = line.strip().split("=")
        if key == "EMAIL_PASSWORD":
            MY_PASSWORD = value
            

def update_api_data():
    global iss_latitude, iss_longitude, sunrise, sunset, MY_LAT, MY_LONG, time_now
    
    g = geocoder.ip('me')
    MY_LAT = g.latlng[0]
    MY_LONG = g.latlng[1] 

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid":"Asia/Kolkata"
    }
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()


def send_mail():
    print("\n------------------------------\n")
    print(f"Current Time: {time_now}")
    print(f"Sunrise: {sunrise}, Sunset: {sunset}")
    print(f"MY_LAT: {MY_LAT}, MY_LONG: {MY_LONG}")
    print(f"iss_latitude: {iss_latitude}, iss_longitude: {iss_longitude}")
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=MY_EMAIL,
                                    msg="Subject:Look Up👆\n\nThe ISS is above you."
                                    )

while True:
    update_api_data()
    send_mail()
    time.sleep(60)
                
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



