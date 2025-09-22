*** Settings ***

Documentation        aLL THE PAGE OBJECTS AND KEYWORD OF LANDING PAGE resource file can be use in our robot file
Library    SeleniumLibrary



*** Variables ***
${page_Tittle}    xpath://a[text()='ProtoCommerce']



*** Keywords ***



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

    Click Element        (//button[@class='btn btn-info'])[${index}]
    Click Element    //a[@class='nav-link btn btn-primary']
    Sleep    3
