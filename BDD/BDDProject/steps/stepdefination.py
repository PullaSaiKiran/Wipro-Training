from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given("buyer is on the OLX homepage")
def step_impl(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.get("https://www.olx.com")

@when("buyer types product in search input")
def step_impl(context):
    # Adjust locator after inspecting OLX site
    searchbar = context.driver.find_element(By.ID, "searchBox")
    searchbar.send_keys("Cars")
    searchbar.send_keys(Keys.ENTER)

@then("search results should be displayed")
def step_impl(context):
    assert "Cars" in context.driver.title and "cars" in context.driver.current_url, "Search Failed"
    heading = context.driver.find_element(By.CSS_SELECTOR, "#maincontext h1")
    assert "Cars" in heading.text, "Search Failed"
    context.driver.quit()
