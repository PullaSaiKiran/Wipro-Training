from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LaptopsCategoryPage(BasePage):
    LAPTOP_LIST = (By.CSS_SELECTOR, ".card-title")

    def verify_laptop_list_presence(self):
        # Wait until at least one laptop card is visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.LAPTOP_LIST)
        )
        elements = self.driver.find_elements(*self.LAPTOP_LIST)
        assert len(elements) > 0, "No laptops found!"
        return True
