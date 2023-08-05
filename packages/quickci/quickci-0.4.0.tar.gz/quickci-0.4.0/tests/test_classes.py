#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import unittest
from unittest.mock import Mock

from quickci.classes import _CIService, TravisCI


class Test_CIService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = _CIService(token="test_token",
                             url="https://www.example.com",
                             branch="master",
                             repo="test_repo")
        self.colours = {"passed": "green", "success": "green",
                        "SUCCESSFUL": "green", "failed": "red",
                        "errored": "red", "FAILED": "red",
                        "started": "yellow", "running": "yellow",
                        "INPROGRESS": "yellow", "ENQUEUED": "yellow"}

    def test_colours(self):
        self.assertEqual(self.colours, self.service.colours)


class TestTravisCI(unittest.TestCase):
    def setUp(self) -> None:
        self.service = TravisCI(token="test_token",
                                branch="master",
                                repo="test_repo")
        self.headers = {"Travis-API-Version": "3",
                        "User-Agent": "quickCI",
                        "Authorization": f"token test_token"}

    def test_headers(self):
        self.assertEqual(self.headers, self.service.headers)

