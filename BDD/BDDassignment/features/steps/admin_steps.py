from behave import given, when, then
from pages.admin_page import AdminPage

@given("I navigate to the Admin module")
def step_open_admin_module(context):
    context.admin_page = AdminPage(context.driver)
    context.admin_page.open_admin_module()

@when("I search for users with the following parameters:")
def step_search_users(context):
    # context.table gives access to the Data Table
    for row in context.table:
        username = row["Username"]
        role = row["UserRole"]
        status = row["Status"]
        context.admin_page.search_user(username, role, status)

@then('I should see the search results containing "{username}"')
def step_verify_search_results(context, username):
    results = context.admin_page.get_search_results()
    assert any(username in r for r in results), f"Expected {username} in results, got {results}"
