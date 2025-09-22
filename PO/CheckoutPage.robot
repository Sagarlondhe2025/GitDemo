*** Settings ***
Library     SeleniumLibrary


*** Variables ***


*** Keywords ***

Procced with checkout
    [Arguments]    ${countryName}
    Click Button    //button[@class='btn btn-success']
    Wait Until Element Is Visible    xpath://input[@id='country']
    Input Text    xpath://input[@id='country']        ${countryName}
    Sleep    10
    Wait Until Element Is Visible    xpath://div[@class='suggestions']
    Click Element    xpath://div[@class='suggestions']
    Sleep    10

    Select Checkbox    //div[@class='checkbox checkbox-primary']/label
    Checkbox Should Be Selected    //div[@class='checkbox checkbox-primary']/label
    Click Button    xpath: //input[@type='submit']
    Element Text Should Be    xpath://*[contains(text(),'Success!')]         Success!
