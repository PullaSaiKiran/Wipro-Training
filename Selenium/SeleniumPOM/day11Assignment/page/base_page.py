# page/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_header(self):
        """Return the text of the first visible <h6> header on the page."""
        header = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h6"))
        )
        return header.text

    def click_element(self, locator):
        """Click an element once it is clickable."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def enter_text(self, locator, text, clear_first=True):
        """Enter text into an input field."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear_first:
            element.clear()
        element.send_keys(text)
        return element

    def get_elements_text(self, locator):
        """Return a list of text values for all elements matching locator."""
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return [el.text for el in elements]
