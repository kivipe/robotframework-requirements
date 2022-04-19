*** Settings ***
Library        ${CURDIR}/../src/RequirementsLibrary

*** Test Cases ***
Check libraries without arguments
    Check Libraries

Check libraries with filename
    Check Libraries    requirements.txt


Check libraries with path
    Check Libraries    ${CURDIR}/requirements.txt

Check libraries incorrect path
    Run Keyword And Expect Error   Cannot find file*
    ...                            Check Libraries    ${CURDIR}/requirements-missing.txt

Check libraries package missing
    Run Keyword And Expect Error   Packages have incorrect versions or are missing. Check logs
    ...                            Check Libraries    ${CURDIR}/requirements-test.txt


