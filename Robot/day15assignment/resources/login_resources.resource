*** Variables ***
${USERNAME_FIELD}    id:user-name
${PASSWORD_FIELD}    id:password
${LOGIN_BUTTON}      id:login-button
${ERROR_MESSAGE}     css:.error-message-container

*** Keywords ***
Login To Application
    [Arguments]    ${username}    ${password}
    Input Text    ${USERNAME_FIELD}    ${username}
    Input Text    ${PASSWORD_FIELD}    ${password}
    Click Button  ${LOGIN_BUTTON}

Invalid Login Scenario
    [Arguments]    ${username}    ${password}    ${expected_error}
    Login To Application    ${username}    ${password}
    Wait Until Element Is Visible    ${ERROR_MESSAGE}    timeout=5s
    ${actual_error}=    Get Text    ${ERROR_MESSAGE}
    Should Be Equal    ${actual_error}    ${expected_error}
