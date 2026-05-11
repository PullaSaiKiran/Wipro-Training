from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # wait up to 10 seconds
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.error_message = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")

    def enter_username(self, username):
        elem = self.wait.until(EC.visibility_of_element_located(self.username_input))
        elem.send_keys(username)

    def enter_password(self, password):
        elem = self.wait.until(EC.visibility_of_element_located(self.password_input))
        elem.send_keys(password)

    def click_login(self):
        elem = self.wait.until(EC.element_to_be_clickable(self.login_button))
        elem.click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text
