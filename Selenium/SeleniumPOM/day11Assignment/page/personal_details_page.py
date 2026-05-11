from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PersonalDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_header(self):
        header = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Personal Details']"))
        )
        return header.text

    def get_employee_name(self):
        name_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='firstName']"))
        )
        return name_field.get_attribute("value")
