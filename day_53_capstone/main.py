from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

GOOGLE_FORM_URL ="https://docs.google.com/forms/d/e/1FAIpQLSdGU_JuOsqvONY0R4Zt2p4A9A0R3uiOB6r6rLN1DREn38jMSg/viewform?usp=publish-editor"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_URL)
form_data = response.content
soup = BeautifulSoup(form_data,'html.parser')
driver = webdriver.Firefox()

# print(soup.prettify())
def insert_to_google_form(address,price,link):
    driver.get(GOOGLE_FORM_URL)
    wait = WebDriverWait(driver,30)
    
    address_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//input[@jsname='YPqjbf'])[1]")
    ))
    price_input = driver.find_element(By.XPATH, "(//input[@jsname='YPqjbf'])[2]")
    link_input = driver.find_element(By.XPATH, "(//input[@jsname='YPqjbf'])[3]")
    
    address_input.send_keys(address)
    price_input.send_keys(price)
    link_input.send_keys(link)
    
    submit_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@jsname='M2UYVd']")
    ))
    submit_btn.click()
    time.sleep(3)
    
for card in soup.find_all('article', {'data-test': 'property-card'}):
    address = card.find('address', {'data-test': 'property-card-addr'}).get_text()
    price = card.find('span', {'data-test': 'property-card-price'}).get_text()
    link = card.find('a', {'data-test': 'property-card-link'}).get('href')
    insert_to_google_form(address,price,link)
    

    