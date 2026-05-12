
*** Settings ***
Library    SeleniumLibrary
Library    ../Libraries/ProductPage.py
Resource   ../Resources/login_resources.resource
Resource   ../Resources/common.resource

Suite Setup    Open Browser To SauceDemo
Test Teardown  Teardown With Screenshot


*** Test Cases ***
Verify Product Prices
    Login To Application    standard_user    secret_sauce
    Wait Until Page Contains    Products

    ${backpack_price}=    Get Product Price By Name    Sauce Labs Backpack
    ${bike_light_price}=  Get Product Price By Name    Sauce Labs Bike Light

    ${total}=    Evaluate    ${backpack_price} + ${bike_light_price}
    Should Be Equal As Numbers    ${total}    39.98
