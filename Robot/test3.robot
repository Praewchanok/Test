*** Settings ***
Library    Browser

*** Variable ***
${URL}    https://www.google.co.th/

*** Keywords ***
Open Webpage
    New Browser    headless=False
    New Page    ${URL}

Input Notebook Therapy 
    Type Text    //*[@class="gLFyf gsfi"]    Notebook Therapy

Enter Search
    Press Keys    //*[@class="gLFyf gsfi"]    Enter

*** Test Case ***
