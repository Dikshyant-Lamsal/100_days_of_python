from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from datetime import datetime

date=datetime.now().strftime('%a %d %b %Y, %I:%M%p')
options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH,value="/html/body/div[3]/div/div[3]/main/div[3]/div[3]/div[2]/div[1]/div/div[3]/ul/li[2]/a[1]")
print(f"Total No of articles on wikipedia as of {date} is {article_count.text}")
