from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.XPATH, "//label[text()='Username']/../following-sibling::div//input")
        self.user_role_dropdown = (By.XPATH, "//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        self.status_dropdown = (By.XPATH, "//label[text()='Status']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        self.search_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_field)
        ).send_keys(username)

    def select_user_role(self, role):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.user_role_dropdown)
        ).click()
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']//span[text()='{role}']"))
        )
        option.click()

    def select_status(self, status):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.status_dropdown)
        ).click()
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']//span[text()='{status}']"))
        )
        option.click()

    def click_search(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()
