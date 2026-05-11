from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.my_info_menu = (By.XPATH, "//span[text()='My Info']")
        self.nickname_input = (By.NAME, "nickName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.toast_message = (By.XPATH, "//p[contains(@class,'oxd-text--toast-message')]")
        self.profile_picture_input = (By.XPATH, "//input[@type='file']")
        self.displayed_nickname = (By.XPATH, "//p[@class='oxd-text oxd-text--p']")  # adjust if needed
        self.profile_picture_img = (By.XPATH, "//img[contains(@class,'employee-image')]")

    def open_my_info(self):
        self.wait.until(EC.element_to_be_clickable(self.my_info_menu)).click()
        # Wait until Personal Details header is visible
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Personal Details']")))

    def update_nickname(self, nickname):
        elem = self.wait.until(EC.visibility_of_element_located(self.nickname_input))
        elem.clear()
        elem.send_keys(nickname)
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def upload_photo(self, file_path):
        file_input = self.wait.until(EC.presence_of_element_located(self.profile_picture_input))
        file_input.send_keys(file_path)
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def get_toast_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.toast_message)).text

    def get_displayed_nickname(self):
        return self.wait.until(EC.visibility_of_element_located(self.displayed_nickname)).text

    def is_profile_picture_updated(self):
        img = self.wait.until(EC.visibility_of_element_located(self.profile_picture_img))
        return img.get_attribute("src") is not None and "default" not in img.get_attribute("src")
