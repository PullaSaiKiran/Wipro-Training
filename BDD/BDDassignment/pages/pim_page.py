from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.add_employee_button = (By.XPATH, "//a[text()='Add Employee']")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")

        # On profile page after save
        self.first_name_field = (By.NAME, "firstName")
        self.last_name_field = (By.NAME, "lastName")

    def open_pim_module(self):
        self.wait.until(EC.element_to_be_clickable(self.pim_menu)).click()

    def click_add_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.add_employee_button)).click()

    def enter_first_name(self, first_name):
        elem = self.wait.until(EC.visibility_of_element_located(self.first_name_input))
        elem.clear()
        elem.send_keys(first_name)

    def enter_last_name(self, last_name):
        elem = self.wait.until(EC.visibility_of_element_located(self.last_name_input))
        elem.clear()
        elem.send_keys(last_name)

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def get_first_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.first_name_field)).get_attribute("value")

    def get_last_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.last_name_field)).get_attribute("value")
