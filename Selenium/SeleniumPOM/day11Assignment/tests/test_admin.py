import pytest
from day11Assignment.page.login_page import LoginPage
from day11Assignment.page.admin_page import AdminPage

@pytest.mark.parametrize("username", ["Admin", "ESS", "John.Smith"])
def test_user_exists(driver, username):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    LoginPage(driver).login("Admin", "admin123")

    admin_page = AdminPage(driver)
    admin_page.side_menu.click_admin()   # navigate via sidebar

    assert admin_page.user_exists(username), f"User {username} not found in table"
