import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    """This class is responsible for sending notifications."""

    def __init__(self):
        self.client = Client(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN")
        )
        self.sender_no = os.getenv("TWILIO_PHONE_NUMBER")
        self.receiver_no = os.getenv("RECEIVER_PHONE_NUMBER")

    def send_message(self, price, date, city):
        message = self.client.messages.create(
            from_=self.sender_no,
            to=self.receiver_no,
            body=(
                f"🚨 Low price alert!\n"
                f"Only ₹{price} to fly to {city}!\n"
                f"Departure Date: {date}\n"
                f"Book now before the price goes up! ✈️"
            )
        )
        print(f"Message sent! SID: {message.sid}")