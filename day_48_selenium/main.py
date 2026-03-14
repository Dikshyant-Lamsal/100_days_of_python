from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)
driver.get("https://www.python.org/")
upcoming_events = driver.find_elements(By.XPATH,value='/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li')
events_dict = {}

for event in upcoming_events:
    e = event.find_element(By.CSS_SELECTOR, "a").text
    d = event.find_element(By.CSS_SELECTOR, "time").text
    events_dict[e] = d 
    
for event,date in events_dict.items():
    print(f"Event : {event}")
    print(f"Date  : {date}")
    print("-" * 30)

driver.quit()