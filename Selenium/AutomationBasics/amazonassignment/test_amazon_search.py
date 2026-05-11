import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()   # or webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_amazon_search(driver):
    # Step 1: Open Amazon
    driver.get("https://www.amazon.in")

    # Step 2: Locate search bar by ID and enter text
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.clear()
    search_box.send_keys("Wireless Headphones")

    # Step 3: Locate search button by XPath and click
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='nav-search-submit-button']"))
    )
    search_button.click()

    # Step 4: Verify results page contains expected text
    results_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Wireless Headphones')]"))
    )
    assert "Wireless Headphones" in results_header.text, "Search results not displayed correctly"
    print("Search results page verified successfully.")
