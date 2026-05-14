*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/login_resources.resource

Suite Setup    Open Browser    https://www.saucedemo.com    edge
Suite Teardown    Close Browser

*** Test Cases ***
Verify Product Prices
    [Tags]    Regression
    Set Test Documentation    Verify that product prices are displayed correctly.
    Login To Application    standard_user    secret_sauce
    Page Should Contain    $29.99
