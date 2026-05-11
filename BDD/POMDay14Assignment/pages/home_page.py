from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.category_page import CategoryPage
from pages.laptops_category_page import LaptopsCategoryPage
from pages.login_modal import LoginModal
from pages.product_details_page import ProductDetailsPage


class HomePage(BasePage):
    LAPTOPS_LINK = (By.LINK_TEXT, "Laptops")
    PHONES_LINK = (By.LINK_TEXT, "Phones")
    SONY_VAIO_I5 = (By.LINK_TEXT, "Sony vaio i5")
    def click_laptops(self):
        self.click(self.LAPTOPS_LINK)
        return LaptopsCategoryPage(self.driver)

    def click_phones(self):
        self.click(self.PHONES_LINK)
        return CategoryPage(self.driver)



    def click_sony_vaio_i5(self):
        self.click(self.SONY_VAIO_I5)
        return ProductDetailsPage(self.driver)

    LOGIN_LINK = (By.ID, "login2")

    def open_login_modal(self):
        self.click(self.LOGIN_LINK)
        return LoginModal(self.driver)