from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.leave_type_dropdown = (By.XPATH, "//label[text()='Leave Type']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        self.from_date_field = (By.XPATH, "//label[text()='From Date']/../following-sibling::div//input")
        self.to_date_field = (By.XPATH, "//label[text()='To Date']/../following-sibling::div//input")
        self.apply_button = (By.XPATH, "//button[text()='Apply']")
        self.toast_message = (By.CLASS_NAME, "oxd-toast-content")
        self.leave_balance = (By.XPATH, "//div[@class='leave-balance']")

    def select_leave_type(self, leave_type):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.leave_type_dropdown)
        ).click()
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']//span[text()='{leave_type}']"))
        )
        option.click()

    def enter_dates(self, from_date, to_date):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_date_field)
        ).send_keys(from_date)
        self.driver.find_element(*self.to_date_field).send_keys(to_date)

    def apply_leave(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.apply_button)
        ).click()

    def get_toast_message(self):
        toast = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.toast_message)
        )
        return toast.text

    def get_leave_balance(self):
        balance_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.leave_balance)
        ).text
        return int(balance_text)
