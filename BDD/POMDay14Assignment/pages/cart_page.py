from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.purchase_modal import PurchaseModal

class CartPage(BasePage):
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Place Order']")

    def click_place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)
        return PurchaseModal(self.driver)
