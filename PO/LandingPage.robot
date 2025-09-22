*** Settings ***

Documentation        aLL THE PAGE OBJECTS AND KEYWORD OF LANDING PAGE resource file can be use in our robot file
Library    SeleniumLibrary



*** Variables ***
${Error_message_login}    xpath: //div[@class='alert alert-danger col-md-12']



*** Keywords ***
fill the login form
    [Arguments]    ${username}    ${password}
    Input Text    id:username       ${username}
    Input Password    id:password    ${password}
    Click Button    signInBtn

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

verify the error message
#    ${result}=    Get Text    ${Error_message_login}
#    Should Be Equal As Strings     ${result}        Incorrect username/password.
#     OR
    Element Text Should Be    ${Error_message_login}    Incorrect username/password.