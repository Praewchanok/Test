*** Settings ***
Library  Selenium2Library

*** Variable ***
${browser}  https://www.google.co.th/?gws_rd=cr&dcr=0&ei=_U4KWoeNFIntvgTM_Y-IDQ
${url}  chrome
*** Keywords ***

*** Test Case ***
1. เปิดเว็บไซต์ google
    Open Browser  ${browser}  ${url}
    Maximize Browser Window
    Set Selenium Speed  0.3
2. กรอกคำว่า มหาวิทยาลัยเกษตรศาสตร์
    Input Text  name=q  มหาวิทยาลัยเกษตรศาสตร์
3. กดค้นหา
    Click Button  name=btnK
4. คลิ๊กไปที่ KU-จำแนกตามคณะ
    Click Element  //*[@id="rso"]/div[1]/div/table/tbody/tr[3]/td/div/h3/a