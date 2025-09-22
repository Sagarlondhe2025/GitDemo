*** Settings ***

Documentation    To Validate Login Form
Library    SeleniumLibrary
Test Setup    open the browser with mortigate payment url
Test Teardown    Close Browser Session
Resource        resource.robot
Library    Collections

*** Variables ***
${Error_message_login}    xpath: //div[@class='alert alert-danger col-md-12']
${page_Tittle}    xpath://a[text()='ProtoCommerce']


*** Test Cases ***

Validate Login Form
    fill the login form    ${user_name}    ${invalid_password}
    Wait Until Element Is Located In Page            ${Error_message_login}
    verify the error message

Validate Cards Display in Shopping Page
    Fill The Login Form    ${user_name}    ${valid_password}
    Sleep    5
    Wait Until Element Is Located In Page    ${page_Tittle}
    validate the cards on page
    select the cards    Nokia Edge

Login with User Tab
    Fill the form and select user    ${user_name}    ${valid_Password}




*** Keywords ***
fill the login form
    [Arguments]    ${username}    ${password}
    Input Text    id:username       ${username}
    Input Password    id:password    ${password}
    Click Button    signInBtn

wait until element is located in page
    [Arguments]    ${element}
    Wait Until Element Is Visible    ${element}

verify the error message
#    ${result}=    Get Text    ${Error_message_login}
#    Should Be Equal As Strings     ${result}        Incorrect username/password.
#     OR
    Element Text Should Be    ${Error_message_login}    Incorrect username/password.


validate the cards on page
    @{expected_list}=    Create List    iphone X    Samsung Note 8    Nokia Edge    Blackberry
    @{elements}=    Get Webelements    //h4[@class='card-title']
    @{actual_list}=    Create List

    FOR    ${element}    IN    @{elements}
        log    ${element.text}
        Append To List    ${actual_list}    ${element.text}
    END
    Log List    ${actual_list}
    Lists Should Be Equal    ${expected_list}    ${actual_list}
    
select the cards
    [Arguments]        ${card_name}

    ${elements}=    Get Webelements    //h4[@class='card-title']
    ${index}=    Set Variable    1
    FOR    ${element}    IN    @{elements}
        Log    ${element.text}
        Exit For Loop If        '${card_name}' == '${element.text}'
            ${index}=    Evaluate        ${index} + 1
    END

    Click Button    (//button[@class='btn btn-info'])[${index}]
    Sleep    3

    
    
Fill the form and select user
    [Arguments]    ${username}    ${password}
    Input Text    id:username     ${username}
    Input Password    id:password    ${password}
    Click Element    xpath://input[@value='user']

    Wait Until Element Is Visible    id:okayBtn
    Click Button    id:okayBtn
    Wait Until Element Is Not Visible    id:okayBtn
    Select From List By Value    //select[@class='form-control']        teach
    
    Select Checkbox    //input[@id='terms']
    Checkbox Should Be Selected    //input[@id='terms']                # ensure Checkbox is selected
    Click Button    signInBtn
    Sleep    3


