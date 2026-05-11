import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from day11Assignment.page.login_page import LoginPage



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login_page = LoginPage(driver)

    login_page.login("Admin", "admin123")

    # Assertion after synchronization
    dashboard_text = driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
    assert dashboard_text == "Dashboard"