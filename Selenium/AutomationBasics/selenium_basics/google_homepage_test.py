# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
#
# # Ask user which browser to open
# browser_choice = input("Enter browser (chrome/edge): ").lower()
#
# match browser_choice:
#     case "chrome":
#         driver = webdriver.Chrome(service=ChromeService("../resources/chromedriver.exe"))
#     case "edge":
#         driver = webdriver.Edge(service=EdgeService("../resources/msedgedriver.exe"))
#     case _:
#         raise ValueError("Unsupported browser choice! Please enter 'chrome' or 'edge'.")
#
# driver.get("https://www.google.com")
#
# pagetitle = driver.title
#
# if pagetitle == "Google":
#     print("Google Homepage loaded --pass")
# else:
#     print("Google Homepage Not loaded --fail")
#
# sleep(5)
# driver.quit()


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

browser_choice = input("Enter browser (chrome/edge): ").lower()

match browser_choice:
    case "chrome":
        driver = webdriver.Chrome(service=ChromeService("../resources/chromedriver.exe"))
    case "edge":
        driver = webdriver.Edge(service=EdgeService("../resources/msedgedriver.exe"))
    case _:
        raise ValueError("Unsupported browser choice! Please enter 'chrome' or 'edge'.")

driver.get("https://www.google.com")

pagetitle = driver.title
if pagetitle == "Google":
    print("Google Homepage loaded --pass")
else:
    print("Google Homepage Not loaded --fail")

sleep(5)
driver.quit()
