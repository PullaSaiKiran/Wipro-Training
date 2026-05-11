from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CategoryPage(BasePage):
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".card-title")

    def get_all_product_names(self):
        # Wait until products are visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.PRODUCT_NAMES)
        )
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text.strip() for el in elements]
