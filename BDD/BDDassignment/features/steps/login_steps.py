from behave import given, when, then
from pages.login_page import LoginPage
import time

@given("I am on the OrangeHRM login page")
def step_open_login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.login_page = LoginPage(context.driver)

@when('I enter username "{username}"')
def step_enter_username(context, username):
    context.login_page.enter_username(username)

@when('I enter password "{password}"')
def step_enter_password(context, password):
    context.login_page.enter_password(password)

@when("I click the login button")
def step_click_login(context):
    context.login_page.click_login()

@then("I should be redirected to the dashboard")
def step_verify_dashboard(context):
    time.sleep(2)
    assert "dashboard" in context.driver.current_url.lower()

@then('I should see an error message containing "Invalid credentials"')
def step_verify_error(context):
    error_text = context.login_page.get_error_message()
    assert "Invalid credentials" in error_text
@then('I should see "Dashboard" on the page')
def step_verify_dashboard_text(context):
    assert "Dashboard" in context.driver.page_source
from behave import given
from pages.login_page import LoginPage

@given('I am logged into OrangeHRM with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.click_login()
