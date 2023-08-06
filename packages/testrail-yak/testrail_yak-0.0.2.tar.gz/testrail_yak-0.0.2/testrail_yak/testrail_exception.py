#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.testrail import APIError


# TestRail
class TestRailException(APIError):
    pass


class TestRailUserException(TestRailException):
    pass


class TestRailProjectException(TestRailException):
    pass


class TestRailSectionException(TestRailException):
    pass


class TestRailTestSuiteException(TestRailException):
    pass


class TestRailTestCaseException(TestRailException):
    pass


class TestRailTestRunException(TestRailException):
    pass


class TestRailTestPlanException(TestRailException):
    pass


class TestRailTestException(TestRailException):
    pass


class TestRailNewEntityException(TestRailException):
    pass


class TestRailUpdateException(TestRailException):
    pass


class TestRailDeleteException(TestRailException):
    pass


class TestRailSuiteModeException(TestRailException):
    pass
