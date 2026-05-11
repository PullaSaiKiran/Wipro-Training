from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.leave_menu = (By.XPATH, "//span[text()='Leave']")
        self.apply_button = (By.XPATH, "//a[text()='Apply']")
        self.leave_type_dropdown = (By.XPATH, "//div[@class='oxd-select-text-input']")
        self.start_date_input = (By.XPATH, "//input[@placeholder='yyyy-mm-dd'][1]")
        self.end_date_input = (By.XPATH, "//input[@placeholder='yyyy-mm-dd'][2]")
        self.submit_button = (By.XPATH, "//button[@type='submit']")
        self.toast_message = (By.XPATH, "//p[contains(@class,'oxd-text--toast-message')]")
        self.leave_balance = (By.XPATH, "//p[contains(@class,'oxd-text--leave-balance')]")
        self.leave_status = (By.XPATH, "//div[@class='oxd-table-cell-status']")

    def open_leave_module(self):
        self.wait.until(EC.element_to_be_clickable(self.leave_menu)).click()

    def apply_leave(self, leave_type, start_date, end_date):
        # Click Apply
        self.wait.until(EC.element_to_be_clickable(self.apply_button)).click()

        # Re-locate dropdown fresh before clicking
        dropdown = self.wait.until(EC.presence_of_element_located(self.leave_type_dropdown))
        self.wait.until(EC.element_to_be_clickable(self.leave_type_dropdown)).click()

        # Select the leave type option
        option_locator = (By.XPATH, f"//span[text()='{leave_type}']")
        self.wait.until(EC.element_to_be_clickable(option_locator)).click()

        # Enter start date
        start_elem = self.wait.until(EC.visibility_of_element_located(self.start_date_input))
        start_elem.clear()
        start_elem.send_keys(start_date)

        # Enter end date
        end_elem = self.wait.until(EC.visibility_of_element_located(self.end_date_input))
        end_elem.clear()
        end_elem.send_keys(end_date)

        # Click Submit
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()

    def get_toast_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.toast_message)).text

    def get_leave_balance_change(self):
        # Capture balance before and after applying leave
        before = int(self.wait.until(EC.visibility_of_element_located(self.leave_balance)).text.split()[0])
        # After applying leave, refresh or navigate back to balance
        after = int(self.wait.until(EC.visibility_of_element_located(self.leave_balance)).text.split()[0])
        return before, after

    def get_leave_status(self):
        return self.wait.until(EC.visibility_of_element_located(self.leave_status)).text

