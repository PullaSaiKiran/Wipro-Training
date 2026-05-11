# features/environment.py
from selenium import webdriver

def before_scenario(context, scenario):
    # Setup browser before each scenario
    context.driver = webdriver.Chrome()   # or Firefox/Edge depending on your setup
    context.driver.maximize_window()

def after_scenario(context, scenario):
    # Teardown browser after each scenario
    context.driver.quit()
