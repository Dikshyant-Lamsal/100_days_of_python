from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# upcoming_events = driver.find_elements(By.XPATH,value='/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li')
# events_dict = {}

# for event in upcoming_events:
#     e = event.find_element(By.CSS_SELECTOR, "a").text
#     d = event.find_element(By.CSS_SELECTOR, "time").text
#     events_dict[e] = d 
    
# for event,date in events_dict.items():
#     print(f"Event : {event}")
#     print(f"Date  : {date}")
#     print("-" * 30)
# firstname = driver.find_element(By.XPATH,value="/html/body/form/input[1]")
# lastname = driver.find_element(By.XPATH,value="/html/body/form/input[2]")
# email_address = driver.find_element(By.XPATH,value="/html/body/form/input[3]")
# sign_up_btn = driver.find_element(By.XPATH,value="/html/body/form/button")

# firstname.send_keys("Dikshit")
# lastname.send_keys("Bhusal")
# email_address.send_keys("dikshit@gmail.com")
# sign_up_btn.click()
search_bar_entry = driver.find_element(By.NAME, "search")
search_bar_entry.send_keys("Chiya khana jum",Keys.ENTER)
