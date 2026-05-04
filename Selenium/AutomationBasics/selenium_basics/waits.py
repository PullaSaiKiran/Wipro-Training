# from telnetlib import EC
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
driver.get("https://www.google.com")
#
# driver.implicitly_wait(5)
#
# search_box = driver.find_element(By.NAME,"q")
# search_box.send_keys("Explicit Wait")
#
# googlesearch_button = driver.find_element(By.NAME,'btnK')
# googlesearch_button.click()

import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)

# Wait for search box
search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
search_box.send_keys("Implicit Wait")

# Wait for the Google Search button to be clickable
googlesearch_button = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
googlesearch_button.click()

time.sleep(5)
driver.quit()
