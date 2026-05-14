*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/login_resources.resource

Suite Setup    Open Browser    https://www.saucedemo.com    edge
Suite Teardown    Close Browser

*** Test Cases ***
Valid Login Test
    [Tags]    Smoke
    Set Test Documentation    Verify that a valid user can log in successfully.
    Login To Application    standard_user    secret_sauce
    Page Should Contain    Products
