#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..lib.testrail import APIClient
from testrail_yak.project import Project
from testrail_yak.section import Section
from testrail_yak.test import Test
from testrail_yak.test_case import TestCase
from testrail_yak.test_plan import TestPlan
from testrail_yak.test_run import TestRun
from testrail_yak.test_suite import TestSuite
from testrail_yak.user import User


class TestRailYak(APIClient):
    """A class to build on top of Gurock's Python interface

    https://github.com/gurock/testrail-api.git
    """
    def __init__(self, url, uname, passwd):

        super().__init__(url)

        self.client             = APIClient(url)
        self.client.user        = uname
        self.client.password    = passwd
        self.project            = Project(self.client)
        self.section            = Section(self.client)
        self.test               = Test(self.client)
        self.test_case          = TestCase(self.client)
        self.test_plan          = TestPlan(self.client)
        self.test_run           = TestRun(self.client)
        self.test_suite         = TestSuite(self.client)
        self.user               = User(self.client)
