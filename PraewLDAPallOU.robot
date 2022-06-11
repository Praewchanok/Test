*** Settings ***
Resource    ./PraewResource.robot


*** Test Cases ***
TST_F10_1_1_001 Verlify login Ldap Content Provider
    Open Webpage
    Input Username And Password    ${username}    ${password}
    Click Login
    Get Token By URL
    New Page    ${lbl_json_response_on_webpage}
    Verify Response
    Jwt Decode Access Token
    Verify Jwt Decode Access Token
    # Jwt Decode Id Token
    # Verify Jwt Decode Id Token 

