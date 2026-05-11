from behave import given, when, then
from pages.leave_page import LeavePage

@given("I navigate to the Leave module")
def step_open_leave_module(context):
    context.leave_page = LeavePage(context.driver)
    context.leave_page.open_leave_module()

@when('I apply for "{leave_type}" from "{start_date}" to "{end_date}"')
def step_apply_leave(context, leave_type, start_date, end_date):
    context.leave_page.apply_leave(leave_type, start_date, end_date)

@then('I should see a success toast message "{message}"')
def step_verify_toast(context, message):
    toast_text = context.leave_page.get_toast_message()
    assert message in toast_text

@then("my leave balance should be reduced")
def step_verify_leave_balance(context):
    before, after = context.leave_page.get_leave_balance_change()
    assert after < before, f"Expected balance to reduce, before={before}, after={after}"

@then('the leave status should be "{status}"')
def step_verify_leave_status(context, status):
    current_status = context.leave_page.get_leave_status()
    assert current_status == status
