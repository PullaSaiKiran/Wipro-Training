from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day11Assignment.page.personal_details_page import PersonalDetailsPage

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        # Increase timeout to 20s for slower demo site
        self.wait = WebDriverWait(driver, 20)

    def search_employee(self, name):
        # Step 1: Wait for Employee Information header
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Employee Information']"))
        )

        # Step 2: Enter name in Employee Name field
        employee_name_input = self.wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//label[text()='Employee Name']/ancestor::div[contains(@class,'oxd-input-group')]//input"
            ))
        )
        employee_name_input.clear()
        employee_name_input.send_keys(name)

        # Step 3: Click Search
        search_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        search_button.click()

        # Step 4: Wait for record
        employee_locator = (By.XPATH, f"//div[@role='row']//div[contains(text(), '{name}')]")
        employee_row = self.wait.until(EC.element_to_be_clickable(employee_locator))

        # Step 5: Click record
        self.driver.execute_script("arguments[0].scrollIntoView();", employee_row)
        employee_row.click()

        return PersonalDetailsPage(self.driver)
