*** Settings ***
Library     SeleniumLibrary
Library     ../pages/SignupPage.py

*** Keywords ***
Open Demoblaze Application
    Launch Demoblaze Application

Click Signup Menu
    Click Signup Link

Enter Signup Username
    Enter Username

Enter Signup Password
    Enter Password

Click Signup Button
    Click Register Button

Validate Signup Success Message
    Verify Signup Success Alert

Close Application
    Close Browser


Launch Demoblaze Application
    # TODO: implement keyword "Launch Demoblaze Application".
    Fail    Not Implemented


Click Signup Link
    # TODO: implement keyword "Click Signup Link".
    Fail    Not Implemented


Enter Username
    # TODO: implement keyword "Enter Username".
    Fail    Not Implemented

