*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kallee
    Set Password  kalle124
    Set Password Confirmation  kalle124
    Submit Credentials
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle124
    Set Password Confirmation  kalle124
    Submit Credentials
    Registering Should Fail With Message  Username must be atleast 3 letters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kallee
    Set Password  kalleyksi
    Set Password Confirmation  kalleyksi
    Submit Credentials
    Registering Should Fail With Message  Password must not have only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kallee
    Set Password  kalle123
    Set Password Confirmation  kalle124
    Submit Credentials
    Registering Should Fail With Message  Password does not match password confirmation


*** Keywords ***
Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

