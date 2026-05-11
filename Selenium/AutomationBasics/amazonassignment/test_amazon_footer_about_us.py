import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()   # or webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)   # implicit wait for general stability
    yield driver
    driver.quit()

def test_amazon_footer_about_us(driver):
    # Step 1: Open Amazon
    driver.get("https://www.amazon.in")

    # Step 2: Scroll to footer and click "About Us" using CSS selector
    about_us_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='aboutamazon']"))
    )
    about_us_link.click()

    # Step 3: Wait for a specific element on About Us page
    # Example: Find link by its visible text
    careers_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Careers"))
    )

    # Step 4: Print text content to console
    print("Found link text on About Us page:", careers_link.text)

    # Assertion to ensure element is present
    assert careers_link.text == "Careers"
