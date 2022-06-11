*** Settings ***
Resource    ../../TestSuite/PraewResource.robot
Resource    ../../../arcadia.automate.buffet/Library/decode_data.py


*** Keywords ***
Open Webpage
    [Documentation]    Owner: Praew
    ...                open browser and open login webpage
    New Browser    browser=chromium    headless=False
    New Page       ${url_login_ldap}

Input Username And Password
    [Documentation]    Owner: Praew
    ...                input user and password
    [Arguments]    ${username}    ${password}
    Type Text    ${txt_username_ldap}    ${username}
    Type Text    ${txt_password_ldap}    ${password}

# Fill Text Box
#     [Documentation]    Owner: Praew
#     ...                Clears and fills text
#     [Arguments]    ${text}
#     Fill Text    ${txt_access_token}    ${text}
    
Click Login
    [Documentation]    Owner: Praew
    ...                click login and return url
    Click    ${btn_login}    

Get Token By URL    
    [Documentation]    Owner: Praew
    ...                get value of code in ais webpage
    # ${url}    Get Url    matches    ^= ${url_ais}
    ${url}    Get Url    ^=    ${url_ais}       
    Log    ${url}
    @{url_split}    Split String    ${url}    /
    ${uri}    Set Variable    ${url_split}[3]
    ${txt_uri_code}    Remove String    ${uri}    ?code=
    ${url_token}    Replace String    ${url_get_token}    Ui27w4hUVWgsxH3csON64KbJ98E9i85tyE7K27yUQ5BU    ${txt_uri_code}
    Set Test Variable    ${lbl_json_response_on_webpage}    ${url_token}

Verify Value By Key
    [Documentation]    Owner: Praew
    [Arguments]    ${json_data}    ${key}
    ${message}    Get Value Json By Key    ${json_data}    ${key}
    Should Match Regexp    ${message}    .    
    Log     ${message}
    
Verify Response
    [Documentation]    Owner: Praew
    ${text_token}    Get Text    ${txt_code_token}
    ${json_token}    Convert String to JSON    ${text_token}
    Verify Value By Key    ${json_token}    $..access_token
    Verify Value By Key    ${json_token}    $..refresh_token    
    Verify Value By Key    ${json_token}    $..id_token    
    Verify Value Json By Key    ${json_token}    $..token_type     bearer
    Verify Value Json By Key    ${json_token}    $..expires_in    86400
    Verify Value Json By Key    ${json_token}    $..refresh_token_expires_in    86400
    Set Test Variable    ${JSON_TOKEN}    ${json_token}
Text Verlify To Json
    [Documentation]    Owner: Praew
    ${json_verify}    Convert String to JSON    ${text_verify}
    Set Test Variable    ${JSON_Verify}    ${json_verify}
Jwt Decode Access Token            
    ${value}    Get Value Json By Key    ${JSON_TOKEN}    $..access_token   
    ${jwt_Decode}    Jwt Decode Dot Dict    ${value}
    Log    ${jwt_Decode}
    Set Test Variable    ${JWT_DECODE_ACCESS_TOKEN}    ${jwt_Decode}
    Set Test Actual Result    ${jwt_Decode}

Jwt Decode Id Token
    ${value}    Get Value Json By Key    ${JSON_TOKEN}    $..id_token    
    ${jwt_Decode}    Jwt Decode Dot Dict    ${value}
    Log    ${jwt_Decode}
    Set Test Variable    ${JWT_DECODE_ID_TOKEN}    ${jwt_Decode}
    Set Test Actual Result    ${jwt_Decode}

๋๋Jwt Decode Verify Access Token
    ${value}    Get Value Json By Key    ${JSON_Verify}    $..access_token
    ${jwt_Decode}    Jwt Decode Dot Dict    ${value}
    Log    ${jwt_Decode}
    Set Test Variable    ${JWT_DECODE_VERIFY_ACCESS_TOKEN}    ${jwt_Decode}
    Set Test Actual Result    ${jwt_Decode}

Jwt Decode Verify Id Token
    ${value}    Get Value Json By Key    ${JSON_Verify}    $..id_token
    ${jwt_Decode}    Jwt Decode Dot Dict    ${value}
    Log    ${jwt_Decode}
    Set Test Variable    ${JWT_DECODE_VERIFY_ID_TOKEN}    ${jwt_Decode}
    Set Test Actual Result    ${jwt_Decode}       

Verify Jwt Decode Access Token
    # Verify Value Should Be Equal    ${actual_value}     ${expected_value}
    Verify Value By Key    ${JWT_DECODE_ACCESS_TOKEN}    $..iss
    Verify Value By Key    ${JWT_DECODE_ACCESS_TOKEN}    $..sub 
    Verify Value By Key    ${JWT_DECODE_ACCESS_TOKEN}    $..aud
    Verify Value By Key    ${JWT_DECODE_ACCESS_TOKEN}    $..exp
    Verify Value By Key    ${JWT_DECODE_ACCESS_TOKEN}    $..iat
    Verify Value By Key    ${JWT_DECODE_ACCESS_TOKEN}    $..pid
    Verify Value Json By Key    ${JWT_DECODE_ACCESS_TOKEN}    $..uid    425
    Verify Value Json By Key    ${JWT_DECODE_ACCESS_TOKEN}    $..idp    ldap
Verify Jwt Decode Id Token
    
