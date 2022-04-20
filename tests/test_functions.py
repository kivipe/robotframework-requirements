# pylint: disable=duplicate-code, missing-module-docstring, missing-function-docstring
# pylint: disable=protected-access
from collections import namedtuple

from packaging import version

from src.RequirementsLibrary import keywords

Package = namedtuple("Package", "name operator version")

version_1_0_0 = version.parse("1.0.0")
version_1_0_1 = version.parse("1.0.1")
version_1_0_2 = version.parse("1.0.2")
no_version = version.parse("0.0.0")


def test_make_package_equal():
    testpackage = keywords._make_package("testpackage==1.0.0")
    expected = Package("testpackage", "==", version_1_0_0)
    assert testpackage == expected


def test_make_package_greater_or_equal():
    testpackage = keywords._make_package("testpackage>=1.0.0")
    expected = Package("testpackage", ">=", version_1_0_0)
    assert testpackage == expected


def test_make_package_no_version():
    testpackage = keywords._make_package("testpackage")
    expected = Package("testpackage", ">=", no_version)
    assert testpackage == expected


def test_make_package_major_only():
    testpackage = keywords._make_package("testpackage>=1")
    expected = Package("testpackage", ">=", version_1_0_0)
    assert testpackage == expected
