from behave import when, then
from selenium.webdriver.common.by import By
from pages.admin_page import AdminPage

@when("I enter the following search criteria:")
def step_impl(context):
    admin_page = AdminPage(context.driver)
    for row in context.table:
        field = row['Field']
        value = row['Value']
        if field == "Username":
            admin_page.enter_username(value)
        elif field == "User Role":
            admin_page.select_user_role(value)
        elif field == "Status":
            admin_page.select_status(value)
    admin_page.click_search()

@then("Search results should be displayed")
def step_impl(context):
    rows = context.driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
    assert len(rows) > 0, "No search results found!"
