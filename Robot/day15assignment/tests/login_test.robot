*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/login_resources.resource

*** Test Cases ***
Valid Login Test
    Open Browser    https://www.saucedemo.com    chrome
    Login To Application    standard_user    secret_sauce
    Wait Until Page Contains    Products
    [Teardown]    Close Browser
Invalid User Login
    [Tags]    negative    login
    [Documentation]    Verify error message for invalid user
    invalid_user    secret_sauce    Epic sadface: Username and password do not match any user in this service
