*** Settings ***
Library        RequirementsLibrary    ${CURDIR}/../requirements.txt

*** Test Cases ***
Check libraries without arguments
    Check Libraries
