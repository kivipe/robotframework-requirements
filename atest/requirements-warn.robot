*** Settings ***
Library        ${CURDIR}/../src/RequirementsLibrary    ${CURDIR}/requirements-test.txt

*** Test Cases ***
Dummy test
    Log    pass
