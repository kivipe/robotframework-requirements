# Requirements checking library for Robot Framework

![Tests](https://github.com/kivipe/robotframework-requirements/actions/workflows/tests.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/kivipe/robotframework-requirements/badge.svg?branch=coveralls)](https://coveralls.io/github/kivipe/robotframework-requirements?branch=coveralls)

## Introduction

Robotframework-requirements is a library that verifies all packages in
requirements.txt are installed and correct version. If missing or incorrect
versions of packages are found, warning is shown

## Usage

It should be enough to add library to Settings part of your suite and it will
give warnings for incorrect requirements.

```Robot
    *** Settings ***
    Library    RequirementsLibrary
```

In case you have requirements.txt in a different folder, you can give path to
file.

```Robot
    *** Settings ***
    Library    RequirementsLibrary    ${CURDIR}/../requirements.txt
```

It is also possible to run library check during test run.

```Robot
    *** Settings ***
    Library    RequirementsLibrary    ${CURDIR}/../requirements.txt

    *** Test Cases ***
    Test Requirements
        Check Libraries
        Check Libraries    ${CURDIR}/../requirements.txt
```

## Submitting issues

Bugs and enhancements are tracked in the [issue tracker](https://github.com/kivipe/robotframework-requirements/issues).

Before submitting a new issue, it is always a good idea to check is the same bug
or enhancement already reported. If it is, please add your comments to the
existing issue instead of creating a new one.

### Coding style

Coding style is defined in `.editorconfig` file. Configure your editor to use it.

Code must pass checks from black, flake8, pylint and mypy. Markdown files must pass
pymarkdown checker.

## License

This library is released under MIT license.
