*** Settings ***
Library    Collections
Library     RequestsLibrary


*** Variables ***
${base_url}    http://216.10.245.166

*** Test Cases ***
Play around Dictionary
    ${data}=    Create Dictionary    name=sagar    cource=robot    age=20
    log     ${data}
    
    Dictionary Should Contain Key       ${data}    name
    Log    ${data}[name]
    Log    ${data}[cource]
    Log     ${data}[age]
    
    ${c}=    Get From Dictionary    ${data}    name
    Log    ${c}
    ${d}=    Get From Dictionary    ${data}    cource
    ${e}=    Get From Dictionary    ${data}    age


Add book in to database
    &{req_body}=    Create Dictionary      name=RobotFramework    isbn=942244    isle=3540353        author=John
    ${response}=    POST    ${base_url}/Library/Addbook.php        json=${req_body}    expected_status=200
    log    ${response.text}
    Log    ${response.status_code}
    Dictionary Should Contain Key    ${response}    