# coding=utf-8

import unittest

from flask import Response

import app.webapp

class WebappTest(unittest.TestCase):
    def setUp(self):
        self.client = app.webapp.app.test_client()

    def test_root_should_raise_404(self):
        # Assign
        # Acts
        rv: Response = self.client.get('/')

        # Assert
        self.assertTrue(404, rv.status)
