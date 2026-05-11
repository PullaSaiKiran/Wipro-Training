from behave import when, then
from pages.leave_page import LeavePage

@when("I apply for one day leave")
def step_impl(context):
    leave_page = LeavePage(context.driver)
    context.initial_balance = leave_page.get_leave_balance()
    leave_page.select_leave_type("Annual Leave")
    leave_page.enter_dates("2026-05-15", "2026-05-15")
    leave_page.apply_leave()
    context.toast_message = leave_page.get_toast_message()

@then("I should see a success message for leave")
def step_impl(context):
    assert "Success" in context.toast_message, f"Expected 'Success', got: {context.toast_message}"

@then("My leave balance should be reduced by one")
def step_impl(context):
    leave_page = LeavePage(context.driver)
    final_balance = leave_page.get_leave_balance()
    expected_balance = context.initial_balance - 1
    assert final_balance == expected_balance, f"Expected {expected_balance}, got {final_balance}"
