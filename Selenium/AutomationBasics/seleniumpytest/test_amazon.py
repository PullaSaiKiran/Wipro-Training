import time
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.amazon.in')
    time.sleep(5)
    yield driver
    driver.quit()


def test_open_amazon(driver):
    assert "amazon" in driver.current_url.lower(), "URL for Amazon is not correct"
    assert "amazon" in driver.title.lower(), "Title for Amazon is not correct"
    print("\nOpened Amazon Homepage. Title & URL verified")


def test_search_product(driver):
    wait = WebDriverWait(driver, 5)

    # Locate and use the search box
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("wireless mouse")

    # Locate and click the search button
    search_btn = driver.find_element(By.ID, "nav-search-submit-button")
    search_btn.click()

    # Assertions to verify search results
    assert "wireless" in driver.current_url.lower(), "Search results page did not load."
    assert "wireless" in driver.title.lower(), "Search results page did not load."
    print("\nSearch results page loaded successfully")


def test_find_elements_amazon(driver):
    wait = WebDriverWait(driver, 15)

    # Get all product titles on the first page
    product_titles = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.a-text-normal"))
    )

    print(f"\nFound {len(product_titles)} product titles on page one.\n")

    # Print first 5 product titles
    for i, title in enumerate(product_titles[:5], start=1):
        print(f"{i}. {title.text}")

    assert len(product_titles) > 0, 'No products found on Amazon search results'
