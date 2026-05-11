import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PurchaseModal(BasePage):
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[text()='Purchase']")
    SUCCESS_MESSAGE = (By.XPATH, "//h2[contains(text(),'Thank you for your purchase!')]")

    def fill_purchase_form(self, data_dict):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NAME_INPUT))

        with allure.step("Fill Name"):
            self.find(self.NAME_INPUT).send_keys(data_dict["name"])
        with allure.step("Fill Country"):
            self.find(self.COUNTRY_INPUT).send_keys(data_dict["country"])
        with allure.step("Fill City"):
            self.find(self.CITY_INPUT).send_keys(data_dict["city"])
        with allure.step("Fill Card"):
            self.find(self.CARD_INPUT).send_keys(data_dict["card"])
        with allure.step("Fill Month"):
            self.find(self.MONTH_INPUT).send_keys(data_dict["month"])
        with allure.step("Fill Year"):
            self.find(self.YEAR_INPUT).send_keys(data_dict["year"])

        # Wait until Purchase button is clickable
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PURCHASE_BUTTON))
        self.click(self.PURCHASE_BUTTON)

    def verify_success_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )
        return "Thank you for your purchase!" in self.get_text(self.SUCCESS_MESSAGE)
