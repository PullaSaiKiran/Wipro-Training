*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/login_resources.resource

Suite Setup    Open Browser    https://www.saucedemo.com    edge
Suite Teardown    Close Browser

Test Template    Invalid Login Scenario

*** Test Cases ***
Invalid User Login
    [Tags]    Critical    Smoke    Regression
    Set Test Documentation    Verify error message for invalid user login.
    invalid_user    secret_sauce    Epic sadface: Username and password do not match any user in this service

Locked Out User Login
    [Tags]    Critical    Regression
    Set Test Documentation    Verify error message for locked out user login.
    locked_out_user    secret_sauce    Epic sadface: Sorry, this user has been locked out.

Problem User Login
    [Tags]    Regression
    Set Test Documentation    Verify behavior of problem_user account.
    problem_user    secret_sauce    Epic sadface: Username and password do not match any user in this service
