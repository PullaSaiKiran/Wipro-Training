from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.result_rows = (By.CSS_SELECTOR, "div.oxd-table-body div.oxd-table-card")

        # Locators
        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.username_input = (By.XPATH, "//label[text()='Username']/../following-sibling::div//input")
        self.userrole_dropdown = (By.XPATH, "//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        self.status_dropdown = (By.XPATH, "//label[text()='Status']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.result_rows = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")

    def open_admin_module(self):
        self.wait.until(EC.element_to_be_clickable(self.admin_menu)).click()

    def search_user(self, username, role, status):
        # Enter username
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)

        # Select role
        self.wait.until(EC.element_to_be_clickable(self.userrole_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{role}']"))).click()

        # Select status
        self.wait.until(EC.element_to_be_clickable(self.status_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{status}']"))).click()

        # Click search
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()

    def get_search_results(self):
        try:
            rows = self.wait.until(EC.presence_of_all_elements_located(self.result_rows))
            return [row.text for row in rows]
        except:
            return []

