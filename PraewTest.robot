*** Settings ***
Library    JSONLibrary
Resource    ../../arcadia.automate.buffet/APIBuffet/RequestLibrary_APICommonKeywords.robot
# Resource    ../Resources/Keywords/PraewTestKeywords.robot
# Resource    ../Resources/Localized/EN/PraewTestLocalized.robot
# Resource    ../Resources/Testsite/DEV/Testsite.robot
Resource    ../Resources/Variables/PraewTestVariables.robot
# Resource    ../Resources/Schemas/BodySchamas.json

*** Test Cases ***
TST_F7_1_1_001 Client Credentials with client id on backend
    # [Documentation]    Owner: Thanchanok
    # Set Content API Header Client Credentials
    # Set Content API Body Client Credentials
    # Send Request
    # Decode Token
    # Verify Response
    Set Content API Header        key=Content-Type     value=application/x-www-form-urlencoded    append=False
    Log    ${API_HEADER}
    Set Schema API Body        value_json=C:\\Users\\Admin\\OneDrive\\เดสก์ท็อป\\Andromeda\\admd.automate.robot.testing\\Resources\\Schemas\\BodySchamas.json    jsonfile=True
    Log    ${API_BODY}


