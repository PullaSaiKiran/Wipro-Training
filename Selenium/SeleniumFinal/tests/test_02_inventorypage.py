import pytest
from selenium.common import ScreenshotException

from pages.loginpage import LoginPage
from pages.inventorypage import InventoryPage
from utils.csv_reader import CSVReader
from utils.excel_reader import ExcelReader
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil

logger=LogGen.loggen()
@pytest.mark.parametrize(
    "data",
    # CSVReader.read_csv("product_validation_data.csv")
     ExcelReader.read_excel("test_data.xlsx", "product_validation")
)
@pytest.mark.order(4)
def test_product_data(driver, data):
    # Arrange: login is setup
    logger.info(f"trying to login with the {data["username"]},{data["password"]}")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Action: Login
    login_page.login()
    logger.log(f"Page Login")
    product_names = inventory_page.get_product_names()

    # Assert: inventory page contract
    #After DDT
    assert data["product_name"] in product_names, '1 or more Product names are not in the inventory'
    screenshot_path= ScreenshotUtil.capture_screenshot(driver,screenshot_name='login_test')
@pytest.mark.order(5)
def test_logout(driver):
    # Arrange: login is setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Action: Login
    login_page.login()
    inventory_page.logout()

    assert "saucedemo.com" in driver.current_url