#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail_exception import (
    TestRailProjectException,
    TestRailTestSuiteException,
    TestRailNewEntityException
)

from urllib import error as E
import time


class TestSuite:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_test_suites(self, project_id):
        """Get a list of test suites associated with a given project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the test suites
        """
        if not project_id or project_id is None:
            raise TestRailProjectException("Invalid project_id")

        if type(project_id) not in [int, float]:
            raise TestRailProjectException("project_id must be an int or float")

        if project_id <= 0:
            raise TestRailProjectException("project_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_suites/{}".format(project_id))
        except E.HTTPError as httpe:
            print(httpe, "- Failed to get test suites. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_suites/{}".format(project_id))
            except E.HTTPError as httpe:
                print(httpe, "- Failed to get test suites.")
        finally:
            return result

    def get_test_suite(self, suite_id):
        """Get a test suite by suite_id.

        :param suite_id: ID of the test suite
        :return: response from TestRail API containing the test suites
        """
        if not suite_id or suite_id is None:
            raise TestRailProjectException("Invalid suite_id")

        if type(suite_id) not in [int, float]:
            raise TestRailTestSuiteException("suite_id must be an int or float")

        if suite_id <= 0:
            raise TestRailTestSuiteException("suite_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_suite/{}".format(suite_id))
        except E.HTTPError as httpe:
            print(httpe, "- Failed to get test suites. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_suite/{}".format(suite_id))
            except E.HTTPError as httpe:
                print(httpe, "- Failed to get test suites.")
        finally:
            return result

    def add_test_suite(self, project_id, name, description):
        """Add a new test suite to a TestRail project.

        :param project_id: ID of the TestRail project
        :param name: name of the new TestRail test suite
        :param description: description of the test suite
        :return: response from TestRail API containing the newly created test suite
        """
        if not project_id or project_id is None:
            raise TestRailProjectException("Invalid project_id")

        if type(project_id) not in [int, float]:
            raise TestRailProjectException("project_id must be an int or float")

        if project_id <= 0:
            raise TestRailProjectException("project_id must be > 0")

        if not name or name is None:
            raise TestRailNewEntityException("Invalid suite name. Unable to add test suite.")

        if not description or description is None:
            raise TestRailNewEntityException("Invalid description. Unable to add test suite.")

        data = dict(name=name, description=description)

        result = None
        try:
            result = self.client.send_post("add_suite/{}".format(project_id), data)
        except E.HTTPError as httpe:
            print(httpe, "- Failed to add test suite. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_post("add_suite/{}".format(project_id), data)
            except E.HTTPError as httpe:
                print(httpe, "- Failed to add test suite.")
        finally:
            return result
