*** Settings ***

Documentation    To Validate Login Form
Library    SeleniumLibrary
Test Teardown    Close Browser
# Resource

*** Variables ***
${Error_message_login}    xpath: //div[@class='alert alert-danger col-md-12']


*** Test Cases ***

Validate Login Form
    open the browser with mortigate payment url
    fill the login form
    wait until error message display
    verify the error message

*** Keywords ***

open the browser with mortigate payment url
    Create Webdriver    Chrome
    Go To    https://rahulshettyacademy.com/loginpagePractise/
    Sleep    5

fill the login form
    Input Text    id:username       rahulshettyacademy
    Input Password    id:password    12345678
    Click Button    signInBtn

wait until error message display
    Wait Until Element Is Visible    ${Error_message_login}

verify the error message
#    ${result}=    Get Text    ${Error_message_login}
#    Should Be Equal As Strings     ${result}        Incorrect username/password.
#     OR
    Element Text Should Be    ${Error_message_login}    Incorrect username/password.
    
    


