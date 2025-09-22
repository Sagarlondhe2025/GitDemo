*** Settings ***

Documentation    resource file can be use in our robot file


*** Variables ***
${user_name}        rahulshettyacademy
${invalid_password}    12345678
${valid_Password}    learning
${browser_name}        Firefox


*** Keywords ***
open the browser with mortigate payment url
    [Arguments]        ${browsername}
    Create Webdriver    ${browsername}
    Go To    https://rahulshettyacademy.com/loginpagePractise/
    Maximize Browser Window
    Sleep    5

Close Browser Session
    Close Browser
    
wait until element is located in page
    [Arguments]    ${element}
    Wait Until Element Is Visible    ${element}