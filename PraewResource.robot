*** Settings ***
Library    Collections
Library    String
Library    DateTime
Library    OperatingSystem
Library    RequestsLibrary
Library    JSONLibrary
Library    SSHLibrary
Library    Browser 

Resource    ../Resources/Keywords/PraewLDAPallOUKeywords.robot
Resource    ../Resources/Variables/PraewLDAPallOUVariables.robot
Resource    ../Resources/Repositories/PraewLDAPallOURepositories.robot
Resource    ../Resources/Localized/EN/PraewLDAPallOULocalized.robot
Resource    ../Resources/Keywords/Commonkeywords.robot

Resource    ../../arcadia.automate.buffet/APIBuffet/RequestLibrary_APICommonKeywords.robot
Resource    ../../arcadia.automate.buffet/UIBuffet/BrowserLibrary_UICommonKeywords.robot
Library     ../../arcadia.automate.buffet/Library/decode_data.py
