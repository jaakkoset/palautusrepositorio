*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  toope
    Set Password  toope123
    Set Password Confirmation  toope123
    Click Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  to
    Set Password  toope123
    Set Password Confirmation  toope123
    Click Register
    Registering Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  toope
    Set Password  toope12
    Set Password Confirmation  toope12
    Click Register
    Registering Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  toope
    Set Password  toopeabc
    Set Password Confirmation  toopeabc
    Click Register
    Registering Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  toope
    Set Password  toope123
    Set Password Confirmation  toope1234
    Click Register
    Registering Should Fail With Message  Password and password confirmation are different

Register With Username That Is Already In Use
    Set Username  paavo
    Set Password  paavo123
    Set Password Confirmation  paavo123
    Click Register
    Registering Should Fail With Message  User with username paavo already exists

Login After Successful Registration
    Logout
    Login Page Should Be Open
    Set Username  paavo
    Set Password  paavo123
    Click Login
    Login Should Succeed

Login After Failed Registration
    Set Username  ma
    Set Password  matti123
    Set Password Confirmation  matti123
    Click Register
    Registering Should Fail With Message  Username must be at least 3 characters long
    Logout
    Login Page Should Be Open
    Set Username  ma
    Set Password  matti123
    Click Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Click Register
    Click Button  Register

Click Login
    Click Button  Login

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  paavo  paavo123
    Go To Register Page

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Logout
    Go To  ${OHTU_URL}
    Click Button  Logout