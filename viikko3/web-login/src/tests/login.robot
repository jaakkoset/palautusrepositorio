*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  nonexisting_username
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Submit Credentials
    Click Button  Login

Reset Application Create User And Go To Login Page
    Reset Application
    Create User  kalle  kalle123
    Go To Login Page
