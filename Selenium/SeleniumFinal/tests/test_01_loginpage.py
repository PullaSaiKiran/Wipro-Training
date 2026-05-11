import pytest
from pages.loginpage import LoginPage
from utils.csv_reader import CSVReader
from utils.excel_reader import ExcelReader
from utils.logger import LogGen

# from utils.excel_reader import ExcelReader


# @pytest.mark.order(1)
# @pytest.mark.parametrize(
#     "data",
#     CSVReader.read_csv("login_data.csv")
#     # ExcelReader.read_excel("test_data.xlsx", "login_data")
# )
# def test_login(driver, data):
#     login_page = LoginPage(driver)
#     login_page.login(data["username"], data["password"])
#
#     if data["expected_result"] == "success":
#         assert "inventory" in driver.current_url
#     else:
#         assert "inventory" not in driver.current_url
#         assert login_page.read_error_message().__contains__("do not match")

logger=LogGen.loggen()
@pytest.mark.order(1)
@pytest.mark.parametrize(
    "data",
    #CSVReader.read_csv("login_data.csv")
    ExcelReader.read_excel("test_data.xlsx", "login_data")
)
def test_login(driver, data):
    login_page = LoginPage(driver)
    logger.info(f"Login Page is Opened")
    logger.info(f"trying to login with the {data["username"]},{data["password"]}")
    login_page.login(data["username"], data["password"])


    logger.info(f"checking loaed in status")
    if data["expected_result"] == "success":
        assert "inventory" in driver.current_url
        logger.info(f"Login Successfully - Inventory page opened")
    else:
        assert "inventory" not in driver.current_url
        error_msg = login_page.read_error_message()
        assert data["expected_error"] in error_msg
        logger.error(f"Login Faid - Inventory page Not opened")