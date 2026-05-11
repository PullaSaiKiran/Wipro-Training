from day11Assignment.page.admin_page import AdminPage
from day11Assignment.page.leave_page import LeavePage
from day11Assignment.page.login_page import LoginPage

def test_sidebar_navigation(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    LoginPage(driver).login("Admin", "admin123")

    # Navigate to Admin
    admin_page = AdminPage(driver)
    admin_page.side_menu.click_admin()
    assert "Admin" in admin_page.get_header() or "User Management" in admin_page.get_header()

    # Navigate to Leave
    leave_page = LeavePage(driver)
    leave_page.side_menu.click_leave()
    header_text = leave_page.get_header()
    assert "Leave" in header_text or "Assign Leave" in header_text or "Leave List" in header_text
    print(f"Leave page opened, header: {header_text}")
