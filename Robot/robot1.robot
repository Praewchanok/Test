*** Settings ***
Library  Selenium2Library

*** Variable ***
${browser}  https://www.google.co.th/?gws_rd=cr&dcr=0&ei=_U4KWoeNFIntvgTM_Y-IDQ
${url}  chrome
${expect}  ROBOT FRAME WORK
*** Keywords ***

*** Test Case ***
1. เปิดเว็บไซต์ google
    Open Browser  ${browser}  ${url}
    Maximize Browser Window
    Set Selenium Speed  0.3
2. กรอกคำว่า Robot Framework
    Input Text  name=q  Robot Framework
3. กดค้นหา
    Click Button  name=btnK
4. คลิ๊กไปที่ Robot Framework
    Click Element  //h3[@class="LC20lb MBeuO DKV0Md"]
5. เช็คหน้าเว็บ
    ${result}  Get Text  //h1[@class="title"]
    Log To Console  ${result}
    Should Be Equal  ${result}  ${expect}