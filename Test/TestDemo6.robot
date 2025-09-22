*** Settings ***

Documentation    To Validate Login Form
Library    SeleniumLibrary
Library    DataDriver        file=Resources/Data.csv   encoding=Utf-8
Test Teardown    Close Browser
Test Template    Validate Login Form        #IMP IMP IMP
# Resource

*** Variables ***
${Error_message_login}    xpath: //div[@class='alert alert-danger col-md-12']


*** Test Cases ***
Login With User ${username} and Password ${password}        Sagar    1234
     



*** Keywords ***
Validate Login Form                                        #IMP IMP
    [Arguments]    ${username}    ${password}
    open the browser with mortigate payment url
    fill the login form    ${username}    ${password}
    wait until error message display
    verify the error message

open the browser with mortigate payment url
    Create Webdriver    Chrome
    Go To    https://rahulshettyacademy.com/loginpagePractise/
    Sleep    5

fill the login form
    [Arguments]    ${username}    ${password}
    Input Text    id:username       ${username}
    Input Password    id:password    ${password}
    Click Button    signInBtn

wait until error message display
    Wait Until Element Is Visible    ${Error_message_login}

verify the error message
#    ${result}=    Get Text    ${Error_message_login}
#    Should Be Equal As Strings     ${result}        Incorrect username/password.
#     OR
    Element Text Should Be    ${Error_message_login}    Incorrect username/password.
    
    


