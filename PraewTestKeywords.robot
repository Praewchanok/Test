*** Settings ***
Library    Browser
Library    RequestsLibrary
Library    JSONLibrary
Resource    ../../../arcadia.automate.buffet/APIBuffet/RequestLibrary_APICommonKeywords.robot
Resource    ../Schemas/PraewTestSchemas.json
Resource    ../Variables/PraewTestVariables.robot
Resource    ../Localized/EN/PraewTestLocalized.robot
Resource    ../Testsite/DEV/Testsite.robot


*** Keywords ***
Set Content API Header Client Credentials
    [Documentation]    Owner: Thanchanok
    [Arguments]

Set Content API Body Client Credentials

Send Request

Decode Token

Verify Response
