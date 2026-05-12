*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/login_resources.resource

Suite Setup    Open Browser    https://www.saucedemo.com    chrome
Suite Teardown    Close Browser

Test Template    Invalid Login Scenario

*** Test Cases ***
Invalid User Login
    invalid_user    secret_sauce    Epic sadface: Username and password do not match any user in this service

Locked Out User Login
    locked_out_user    secret_sauce    Epic sadface: Sorry, this user has been locked out.

Problem User Login
    problem_user    secret_sauce    Epic sadface: Username and password do not match any user in this service
