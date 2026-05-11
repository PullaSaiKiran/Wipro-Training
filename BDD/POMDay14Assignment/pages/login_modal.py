import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginModal(BasePage):
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.USERNAME_INPUT))

        with allure.step("Enter Username"):
            self.find(self.USERNAME_INPUT).send_keys(username)
        with allure.step("Enter Password"):
            self.find(self.PASSWORD_INPUT).send_keys(password)
        with allure.step("Click Log in"):
            self.click(self.LOGIN_BUTTON)

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text
