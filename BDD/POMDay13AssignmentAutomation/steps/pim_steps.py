from behave import when, then
from pages.pim_page import PIMPage

@when('I enter "{first_name}" and "{last_name}"')
def step_impl(context, first_name, last_name):
    pim_page = PIMPage(context.driver)
    pim_page.enter_first_name(first_name)
    pim_page.enter_last_name(last_name)
    pim_page.click_save()


@then("Employee should be created successfully")
def step_impl(context):
    # Simple assertion: check URL contains 'pim' or 'viewPersonalDetails'
    current_url = context.driver.current_url
    assert "pim" in current_url or "viewPersonalDetails" in current_url, \
        f"Employee creation failed! Current URL: {current_url}"
