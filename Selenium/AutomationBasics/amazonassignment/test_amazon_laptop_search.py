import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()   # or webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)   # Implicit Wait applied globally
    yield driver
    driver.quit()

def test_amazon_laptop_search(driver):
    # Step 1: Open Amazon
    driver.get("https://www.amazon.in")

    # Step 2: Locate search bar and enter laptop model
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys("HP Pavilion Laptop")

    # Step 3: Locate search button by XPath and click
    search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
    search_button.click()

    # Step 4: Explicit Wait for results grid or product image
    wait = WebDriverWait(driver, 10)
    first_result = wait.until(
        EC.visibility_of_element_located((By.XPATH, "(//div[@data-component-type='s-search-result'])[1]"))
    )

    # Step 5: Click the first result
    first_result.click()

    # Step 6: Verify product page loaded
    assert "HP" in driver.title or "Laptop" in driver.title, "Product page did not load correctly"
    print("Laptop product page loaded successfully.")
