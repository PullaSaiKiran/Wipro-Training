from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage

@given("User is on the OrangeHRM login page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.login_page = LoginPage(context.driver)

@when('User enters username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.click_login()

@then("User should be redirected to dashboard")
def step_impl(context):
    current_url = context.driver.current_url
    assert "dashboard" in current_url, f"Login failed! Current URL: {current_url}"
    context.driver.quit()
