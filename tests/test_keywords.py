# pylint: disable=duplicate-code, missing-module-docstring, missing-function-docstring
# pylint: disable=protected-access
from collections import namedtuple

import pytest
from packaging import version

from src.RequirementsLibrary import RequirementsLibrary, keywords

Package = namedtuple("Package", "name operator version")

version_1_0_0 = version.parse("1.0.0")
version_1_0_1 = version.parse("1.0.1")
version_1_0_2 = version.parse("1.0.2")
no_version = version.parse("0.0.0")


def test_compare_versions_ok():
    required = [
        Package(name="foo", operator="==", version=version_1_0_0),
        Package(name="bar", operator="==", version=version_1_0_0),
    ]
    installed = [
        Package(name="foo", operator="==", version=version_1_0_0),
        Package(name="bar", operator="==", version=version_1_0_0),
    ]
    assert keywords._compare_versions(required, installed)


def test_compare_versions_bad():
    required = [
        Package(name="foo", operator="==", version=version_1_0_0),
        Package(name="bar", operator="==", version=version_1_0_0),
    ]
    installed = [Package(name="foo", operator="==", version=version_1_0_0)]
    assert keywords._compare_versions(required, installed) is False


def test_compare_equal():
    required = Package(name="test", operator="==", version=version_1_0_0)
    installed = [Package(name="test", operator="==", version=version_1_0_0)]
    assert keywords._compare_version(required, installed)


def test_compare_greater_accepted():
    required = Package(name="test", operator=">=", version=version_1_0_0)
    installed = [Package(name="test", operator="==", version=version_1_0_1)]
    assert keywords._compare_version(required, installed)


def test_compare_greater_equal_accepted():
    required = Package(name="test", operator=">=", version=version_1_0_0)
    installed = [Package(name="test", operator="==", version=version_1_0_0)]
    assert keywords._compare_version(required, installed)


def test_compare_greater_equal_accepted_by_earlier_installed():
    required = Package(name="test", operator=">=", version=version_1_0_1)
    installed = [Package(name="test", operator="==", version=version_1_0_0)]
    assert keywords._compare_version(required, installed) is False


def test_compare_greater_but_equal_needed():
    required = Package(name="test", operator="==", version=version_1_0_0)
    installed = [Package(name="test", operator="==", version=version_1_0_1)]
    assert keywords._compare_version(required, installed) is False


def test_compare_smaller_but_equal_needed():
    required = Package(name="test", operator="==", version=version_1_0_2)
    installed = [Package(name="test", operator="==", version=version_1_0_1)]
    assert keywords._compare_version(required, installed) is False


def test_compare_no_version():
    required = Package(name="test", operator=">=", version=no_version)
    installed = [Package(name="test", operator="==", version=version_1_0_1)]
    assert keywords._compare_version(required, installed)


def test_compare_bad_operator():
    required = Package(name="test", operator="><", version=no_version)
    installed = [Package(name="test", operator="==", version=version_1_0_1)]
    assert keywords._compare_version(required, installed) is False


def test_compare_missing():
    required = Package(name="test", operator="==", version=version_1_0_0)
    installed = [Package(name="nottest", operator="==", version=version_1_0_0)]
    assert keywords._compare_version(required, installed) is False


def test_init_check():
    requirements = RequirementsLibrary()
    assert requirements.check_libraries() is True


def test_check_libraries_bad():
    requirements = RequirementsLibrary()
    requirements.requirements = [
        Package(name="foo", operator="==", version=version_1_0_0),
        Package(name="bar", operator="==", version=version_1_0_0),
    ]
    requirements.installed = [Package(name="foo", operator="==", version=version_1_0_0)]
    with pytest.raises(Exception):
        requirements.check_libraries()


def test_init_filenotfound():
    with pytest.raises(Exception):
        RequirementsLibrary("qwrety.txt")
