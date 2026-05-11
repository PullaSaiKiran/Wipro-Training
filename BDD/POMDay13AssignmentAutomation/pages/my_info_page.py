from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.upload_input = (By.XPATH, "//input[@type='file']")
        self.toast_message = (By.CLASS_NAME, "oxd-toast-content")

    def upload_profile_picture(self, file_path):
        upload_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.upload_input)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", upload_element)
        upload_element.send_keys(file_path)

    def get_toast_message(self):
        toast = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.toast_message)
        )
        return toast.text
