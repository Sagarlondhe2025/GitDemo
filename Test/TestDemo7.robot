*** Settings ***

Documentation    To Validate Login Form
Library    SeleniumLibrary
Library    ../CustomLibraries/Shop.py
Test Setup    open the browser with mortigate payment url    ${browser_name}
#Test Teardown    Close Browser Session
Resource        ../PO/Generic_resource.robot
Library    Collections
Resource    ../PO/LandingPage.robot
Resource    ../PO/ShopPage.robot
Resource    ../PO/CheckoutPage.robot


*** Variables ***
${card_name}    Nokia Edge
${country_Name}    India
*** Test Cases ***

Validate Login Form
    [Tags]        SMOKE
    LandingPage.fill the login form    ${user_name}    ${invalid_password}
    Generic_Resource.Wait Until Element Is Located In Page            ${Error_message_login}
    LandingPage.verify the error message

Validate Cards Display in Shopping Page
    [Tags]        REGRESSION
    LandingPage.Fill The Login Form    ${user_name}    ${valid_password}
    Sleep    5
    Generic_Resource.Wait Until Element Is Located In Page    ${page_Tittle}
    ShopPage.validate the cards on page
    Hello_Buddies
    ShopPage.select the cards    ${card_name}
    CheckoutPage.Procced with checkout        ${country_Name}


Login with User Tab
    [Tags]    SANITY
    LandingPage.Fill the form and select user    ${user_name}    ${valid_Password}












    

    
    



