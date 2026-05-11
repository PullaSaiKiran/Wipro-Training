import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Setup: Launch browser
    driver = webdriver.Edge()   # or webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown: Close browser
    driver.quit()

def test_amazon_navigation(driver):
    # Step 1: Open Amazon
    driver.get("https://www.amazon.in")

    # Step 2: Verify title contains 'Amazon'
    assert "Amazon" in driver.title, "Title does not contain 'Amazon'"

    # Step 3: Navigate to Mobiles category
    mobiles_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Mobiles"))
    )
    mobiles_link.click()
    assert "Mobile" in driver.title or "Mobiles" in driver.page_source

    # Step 4: Navigate back to homepage
    driver.back()
    assert "Amazon" in driver.title
