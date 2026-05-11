import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ProductDetailsPage(BasePage):
    ADD_TO_CART_BUTTON = (By.LINK_TEXT, "Add to cart")

    def add_product_to_cart(self):
        # Click the Add to cart button
        self.click(self.ADD_TO_CART_BUTTON)

        # Wait for alert to appear
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # Switch to alert and accept
        alert = self.driver.switch_to.alert
        logging.info(f"Alert appeared with text: {alert.text}")
        alert.accept()

        logging.info("Product successfully added to cart.")
        return True
