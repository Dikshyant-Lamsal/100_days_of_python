from bs4 import BeautifulSoup
import requests
import smtplib
import dotenv
import os
import re

dotenv.load_dotenv()
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SENDER_EMAIL="diksclaude1@gmail.com"
RECEIVER_EMAIL="diksclaude1@gmail.com"
WEBSITE_URL = "https://www.amazon.com/PUMA-Tazon-White-Silver-Running/dp/B01G3LZ5HM?crid=19DQVW35LE8AK&dib=eyJ2IjoiMSJ9.MRVewSChw174gyeSXM4lCWHZOx4Kfu09jK66cjPF1idANT3FsFOSRvBpmGfMrW9wb6is4rFBwZTgllnhu9FU7IiNgByyRmCYmYEd7uhoaJiQVrGmWGaK5k-9XXg8Omlk9J1ju_XD8q-BPYcRDq49Tta5xoeQ1OymbKSMq5z8xoneT_dDjA9hXtX0yIHX3y8lqHt2NRldtk8n2loZDWoGxuWrBuYVlpi8S_VQcaQJM4UYN9TNMkJHOXte70XwfcaklsAkkE69zQMS2B3d2pwoC5Envy8yU1Ja5n26caLANOQ.fh1Y7nmve4v_YN4i4nqrO9JHMjYzZZHS5A8O-ZmdzFM&dib_tag=se&keywords=puma&qid=1773332052&sprefix=p%2Caps%2C488&sr=8-7"
MIN_PRICE = 1000
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language":"en-US"
}
data = requests.get(WEBSITE_URL,headers=headers)

soup = BeautifulSoup(data.text,'html.parser')
price = soup.find("span", class_="aok-offscreen").get_text()
price = float(re.search(r'[\d,]+\.\d+', price).group().replace(',', ''))
title = soup.select_one("#productTitle").get_text(strip=True)
item_name = title.split(",")[0] 
print(price)
print(item_name)

def send_email(price):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=SENDER_EMAIL, password=EMAIL_PASSWORD)
                connection.sendmail(from_addr=SENDER_EMAIL,
                                    to_addrs=RECEIVER_EMAIL,
                                    msg=f"Subject:Price Drop on item:{item_name}\n\nThe price has dropped below Rs.{MIN_PRICE} to Rs.{price}."
                                    )

if price<MIN_PRICE:
    send_email(price=price)