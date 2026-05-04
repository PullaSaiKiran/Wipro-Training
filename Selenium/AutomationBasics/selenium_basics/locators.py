# # from time import sleep
# # import time
# # from selenium import webdriver
# # from selenium.webdriver.edge.service import Service
# # from selenium.webdriver.common.by import By
# #
# # driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
# # driver.get("https://www.google.com")
# # #
# # # # Locate the search box by ID
# # # search_input = driver.find_element(By.ID, "APjFqb")
# # # search_input.send_keys("selenium")
# # #
# # # time.sleep(3)
# # #
# # # # Clear the input field
# # # search_input.clear()
# #
# #
# # search_input = driver.find_element(By.NAME,"q")
# # search_input.send_keys("locators")
# # sleep(3)
# # # driver.quit()
# #
# # # googlesearch_button = driver.find_element(By.NAME,"btnK")
# # # googlesearch_button.click()
# # # sleep(30)
# #
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
# driver.get("https://www.google.com")
#
# # Locate the search box
# search_input = driver.find_element(By.NAME, "q")
# search_input.send_keys("locators")
# sleep(2)
# #
# # # Locate the "I'm Feeling Lucky" button
# # feeling_lucky_button = driver.find_element(By.NAME, "btnI")
# # feeling_lucky_button.click()
# #
# # sleep(5)
# # driver.quit()
# #
# # from selenium import webdriver
# # from selenium.webdriver.edge.service import Service
# # from selenium.webdriver.common.by import By
# #
# # driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
# # driver.get("https://www.google.com")
# # #
# # # Get all elements on the page
# # all_elements = driver.find_elements(By.XPATH, "//*")
# #
# # # Count them
# # print("Total number of tags on homepage:", len(all_elements))
# #
# # # Optional: print unique tag names
# # unique_tags = set([elem.tag_name for elem in all_elements])
# # print("Unique tags:", unique_tags)
# #
# # driver.quit()
#
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
# driver.get("https://www.google.com")
#
# # Find all anchor tags
# href_elements = driver.find_elements(By.TAG_NAME, "a")
#
# # Loop through and print text + href
# for elmt in href_elements:
#     print(f'{elmt.text} - {elmt.get_attribute("href")}')
#
# driver.quit()
# import time
#
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
# driver.get("https://www.google.com")
#
# # images_links = driver.find_element(By.LINK_TEXT,"Images")
# # images_links.click()
# # time.sleep(10)
#
# # images_link = driver.find_element(By.PARTIAL_LINK_TEXT,"Ima")
# # images_link.click()
# # time.sleep(10)
#
# search_input = driver.find_element(By.CSS_SELECTOR,'div > textarea')
# search_input.send_keys('selenium')
# time.sleep(5)
from traceback import clear_frames

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from time import sleep
#
# driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
# driver.get("https://www.google.com")

# Locate search box using XPath
# search_input = driver.find_element(By.XPATH, "//textarea[@name='q']")
# search_input.send_keys("Selenium XPath examples")


# settings_text = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/span")
#
# print(settings_text.text)
# sleep(3)
# driver.quit()
# import time
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.common.by import By
#
# # Launch Edge
# driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
# driver.get("https://the-internet.herokuapp.com/tables")
# time.sleep(5)
#
# # AND Example: match text + class
# and_example = driver.find_element(By.XPATH, "//td[text()='Tim' and @class='first-name']")
# print(f'AND Example -> Found with both conditions: {and_example.text}')
#
# # OR Example: match either Tim or Frank
# or_example = driver.find_element(By.XPATH, "//td[text()='Tim'] | //td[text()='Frank']")
# print(f"OR Example -> Found with either condition: {or_example.text}")
#
# # Child Example: count columns in first row
# first_row_columns = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td")
# print(f"Child example -> Found {len(first_row_columns)} columns in the first row of table1.")
#
# # Email Cell Example: locate specific email
# email_cell = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']")
# print(f"Email cell text: {email_cell.text}")
#
# # Parent Row Example: get the row containing that email
# parent_row = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']/parent::tr")
# print(f"Parent row text: {parent_row.text}")
#
#
# # Ancestor example: climb up from a cell to its row
#
# ancestor = driver.find_element(By.XPATH, "//td[text()='jdoe@hotmail.com']/ancestor::table")
# print("Ancestor -> Row text:", ancestor.text)
#
# # Descendant example: go down from table to all cells
# descendants = driver.find_elements(By.XPATH, "//table[@id='table1']/descendant::td")
# print("Descendant -> Total cells:", len(descendants))
#
# driver.quit()



#RELATIVE LOCATORS

import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
driver.get("https://www.saucedemo.com/")

# Locate fields directly
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Relative locator: element above password
elmt_above_password = driver.find_element(locate_with(By.TAG_NAME, "input").above(password_field))
print(f"Above Example -> Placeholder above password: {elmt_above_password.get_attribute('placeholder')}")
elmt_above_password.send_keys("standard_user")

time.sleep(2)

# Relative locator: element below username
field_below_username = driver.find_element(locate_with(By.TAG_NAME, "input").below(username_field))
print(f"Below Example -> Placeholder below username: {field_below_username.get_attribute('placeholder')}")
field_below_username.send_keys("secret_sauce")

time.sleep(2)

# Finally click login
login_button.click()
time.sleep(5)

# Social icons on inventory page
twitter_icon = driver.find_element(By.LINK_TEXT, "Twitter")

# Element to the right of Twitter
facebook_icon = driver.find_element(locate_with(By.TAG_NAME, "a").to_right_of(twitter_icon))
print(f"toRightOf Example -> Element to the right of Twitter icon has href: {facebook_icon.get_attribute('href')}")

# Element to the left of Facebook
left_icon = driver.find_element(locate_with(By.TAG_NAME, "a").to_left_of(facebook_icon))
print(f"toLeftOf Example -> Element to the left of Facebook icon has href: {left_icon.get_attribute('href')}")

# Elements near Facebook
near_twitter = driver.find_elements(locate_with(By.TAG_NAME, "a").near(facebook_icon))
for element in near_twitter:
    print(f"Near Example -> Element near Facebook icon has href: {element.get_attribute('href')}")

time.sleep(3)
driver.quit()


