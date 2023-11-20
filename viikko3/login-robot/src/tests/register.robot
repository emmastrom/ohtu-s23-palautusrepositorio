*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallee  kalle124
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be atleast 3 letters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle1  kalle123
    Output Should Contain  Username must be only letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  kallee  ka123
    Output Should Contain  Password must be atleast 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallee  kalleyksi
    Output Should Contain  Password must not have only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
