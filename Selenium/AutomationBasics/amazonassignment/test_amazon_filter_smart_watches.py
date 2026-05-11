import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()   # or webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.mark.parametrize("brand", ["boAt","Fastrack", "Noise"])
def test_amazon_filter_smart_watches(driver, brand):
    # Step 1: Open Amazon
    driver.get("https://www.amazon.in")

    # Step 2: Search for Smart Watches
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Smart Watches")
    driver.find_element(By.ID, "nav-search-submit-button").click()

    # Step 3: Locate and click Brand filter dynamically
    brand_filter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[text()='{brand}']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", brand_filter)
    brand_filter.click()

    # Step 4: Wait for results grid to refresh
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
    )

    # Step 5: Count products displayed on first page
    products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    print(f"Brand: {brand} → Products found: {len(products)}")

    # Assertion: Ensure at least one product is displayed
    assert len(products) > 0, f"No products found for brand {brand}"
