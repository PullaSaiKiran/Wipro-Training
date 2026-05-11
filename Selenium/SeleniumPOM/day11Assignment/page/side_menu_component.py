from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SideMenuComponent:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_admin(self):
        admin_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))
        )
        admin_link.click()

    def click_pim(self):
        pim_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))
        )
        pim_link.click()

    def click_leave(self):
        leave_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']"))
        )
        leave_link.click()

    def logout(self):
        logout_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'logout')]"))
        )
        logout_link.click()

    def search_menu(self, text):
        search_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
        )
        search_input.clear()
        search_input.send_keys(text)
