from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day11Assignment.page.side_menu_component import SideMenuComponent
from day11Assignment.page.base_page import BasePage

class AdminPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)   # sets self.driver and self.wait
        self.side_menu = SideMenuComponent(driver)   # <-- add this

    def get_all_usernames(self):
        # Wait until table is visible
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='oxd-table-body']"))
        )
        username_elements = self.driver.find_elements(
            By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']//div[2]"
        )
        return [el.text for el in username_elements]

    def user_exists(self, username):
        return username in self.get_all_usernames()
