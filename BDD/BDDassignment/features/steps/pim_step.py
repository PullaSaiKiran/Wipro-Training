# features/steps/pim_steps.py
from behave import given, when, then
from pages.pim_page import PIMPage

@given("I navigate to the PIM module")
def step_open_pim_module(context):
    context.pim_page = PIMPage(context.driver)
    context.pim_page.open_pim_module()

@given('I click on "Add Employee"')
def step_click_add_employee(context):
    context.pim_page.click_add_employee()

@when('I enter First Name "{first_name}"')
def step_enter_first_name(context, first_name):
    context.pim_page.enter_first_name(first_name)

@when('I enter Last Name "{last_name}"')
def step_enter_last_name(context, last_name):
    context.pim_page.enter_last_name(last_name)

@when("I click the Save button")
def step_click_save(context):
    context.pim_page.click_save()

@then('I should see the employee profile page for "{first_name}" "{last_name}"')
def step_verify_employee_profile(context, first_name, last_name):
    assert context.pim_page.get_first_name() == first_name
    assert context.pim_page.get_last_name() == last_name
