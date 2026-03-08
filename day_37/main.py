import requests
import dotenv  
import os
import datetime

dotenv.load_dotenv(dotenv_path=".env")
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")

pixela_params = {
    "username": USERNAME,
    "token": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#CREATED USER
# response = requests.post("https://pixe.la/v1/users", json=pixela_params)


piexela_graph_header = {
    "X-USER-TOKEN": TOKEN
}

piexela_graph_params = {
    "id": "graph1",
    "name": "Spending Graph",
    "unit": "Rupees",
    "type": "float",
    "color": "momiji"
}

DATE = datetime.datetime.now().strftime("%Y%m%d")

def post_pixel(quantity):
    post_pixel_params = {
        "date": DATE,
        "quantity": quantity
    }
    response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1", json=post_pixel_params, headers=piexela_graph_header)
    print(response.text)

def delete_todays_pixel():
    response = requests.delete(f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{DATE}", headers=piexela_graph_header)
    print(response.text)

val = input("Enter the amount you spent today: ")
post_pixel(val)
