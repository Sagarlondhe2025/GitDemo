*** Settings ***
Documentation    To Validate Login Form
Library    SeleniumLibrary
Test Setup    open the browser with mortigate payment url    ${browser_name}
Test Teardown    Close Browser Session
Resource        resource.robot
Library    Collections
Library    BuiltIn
Library    String

*** Test Cases ***
Verify Child Window
    Click on the Child Window Link
    Verify User is switched to child Window
    Grab The email Id From Child Window
    Enter the main window and Write the Email
*** Keywords ***
Click on the Child Window Link
    Click Element    xpath://a[@class='blinkingText']
    Sleep    5
Verify User is switched to child Window
    Switch Window    NEW
    Element Text Should Be    //h1    DOCUMENTS REQUEST

Grab The email Id From Child Window
#    ${text}=    Get Text    //h1
#    @{words}=    Split String    ${text}
#
#    #PDOCUMENTS REQUEST
#    #0-PDOCUMENTS
#    #1-REQUEST
#    
#    ${split_Text}=    Get From List     ${words}   1
#    Log    ${split_Text}

    ${gmail}=    Get Text    //a[@href='mailto:mentor@rahulshettyacademy.com']
    Log    ${gmail}
    Set Global Variable   ${gmail}

Enter the main window and Write the Email

    Switch Window    MAIN
    Input Text    id:username    ${gmail}
