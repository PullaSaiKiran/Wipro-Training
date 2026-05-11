from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day11Assignment.page.side_menu_component import SideMenuComponent

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   # <-- add this
        self.side_menu = SideMenuComponent(driver)

    def get_header(self):
        header = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h6"))
        )
        return header.text
