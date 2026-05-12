*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Browser To SauceDemo
    Open Browser    https://www.saucedemo.com    chrome
    Maximize Browser Window

Teardown With Screenshot
    Run Keyword If Test Failed    Capture Page Screenshot    failure_${TEST_NAME}_${CURTIME}.png
    Close Browser
