import pytest
from selenium import webdriver
from day11Assignment.page.login_page import LoginPage
from day11Assignment.page.pim_page import PIMPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_view_employee_details(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    LoginPage(driver).login("Admin", "admin123")

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

    pim_page = PIMPage(driver)
    personal_details_page = pim_page.search_employee("Linda Anderson")

    assert personal_details_page.get_header() == "Personal Details"
    print("Test passed: Linda Anderson details page opened")

