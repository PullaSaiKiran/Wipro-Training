
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.amazon.in')
    yield driver
    driver.quit()
