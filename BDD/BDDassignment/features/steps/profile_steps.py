from behave import given, when, then
from pages.profile_page import ProfilePage

@given("I navigate to the My Info section")
def step_open_my_info(context):
    context.profile_page = ProfilePage(context.driver)
    context.profile_page.open_my_info()

@when('I change my Nick Name to "{nickname}"')
def step_change_nickname(context, nickname):
    context.profile_page.update_nickname(nickname)

@when('I upload a profile photograph "{file_path}"')
def step_upload_photo(context, file_path):
    context.profile_page.upload_photo(file_path)


@then('my profile should display the new Nick Name "{nickname}"')
def step_verify_nickname(context, nickname):
    displayed = context.profile_page.get_displayed_nickname()
    assert displayed == nickname

@then("my profile picture should be updated")
def step_verify_profile_picture(context):
    assert context.profile_page.is_profile_picture_updated()

