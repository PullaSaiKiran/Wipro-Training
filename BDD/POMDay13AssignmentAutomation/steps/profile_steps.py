from behave import when, then
from pages.my_info_page import MyInfoPage

@when("I upload my profile picture")
def step_impl(context):
    my_info_page = MyInfoPage(context.driver)
    my_info_page.upload_profile_picture(r"C:\\Users\\Sai\\Pictures\\profile.jpg")
    context.toast_message = my_info_page.get_toast_message()

@then("I should see a success message for profile update")
def step_impl(context):
    assert "Success" in context.toast_message, f"Expected 'Success', got: {context.toast_message}"
