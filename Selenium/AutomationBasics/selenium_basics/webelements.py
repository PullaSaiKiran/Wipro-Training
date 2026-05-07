import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(1)

#Text Input

text_input = driver.find_element(By.ID,"my-text-id")
text_input.clear()
text_input.send_keys("Selenium WebDriver Demo")

#password input

password_input = driver.find_element(By.NAME,"my-password")
password_input.clear()
password_input.send_keys("secret123")


#Text Area
text_area = driver.find_element(By.NAME,"my-textarea")
text_area.clear()
text_area.send_keys("This is simple message")

#check box

checkbox = driver.find_element(By.ID,"my-check-2")
checkbox.click()

#radio Button

radio = driver.find_element(By.ID,"my-radio-2")
radio.click()


#dropdowns

dropdown = driver.find_element(By.NAME,"my-select")
dropdown.click()

option = driver.find_element(By.CSS_SELECTOR,"select[name='my-select'] option[value='2']")
option.click()

#multi-select
multi_select = driver.find_element(By.NAME,"my-datalist")
multi_select.send_keys('New York')


# file-upload
file_upload = driver.find_element(By.NAME, "my-file")
file_upload.send_keys(r"C:\Wipro Training\Selenium\AutomationBasics\selenium_basics\waits.py")

#range slider

range_slider = driver.find_element(By.NAME,'my-range')
driver.execute_script("arguments[0].value=10;",range_slider)

#color picker

color_picker = driver.find_element(By.NAME,"my-colors")
color_picker.send_keys("#00ff00")

# Date picker
date_input = driver.find_element(By.NAME, "my-date")
driver.execute_script("arguments[0].value = '2025-12-25';", date_input)

# Submit button
submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
driver.execute_script("arguments[0].click();", submit_btn)


time.sleep(10)
driver.quit()
