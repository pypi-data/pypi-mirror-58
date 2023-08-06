"""Tests for all_info module."""

import collections.abc
import unittest

from system_query.all_info import query_all


class Tests(unittest.TestCase):

    def test_query_all(self):
        info = query_all(sudo=False)
        self.assertIsInstance(info, collections.abc.Mapping)
        self.assertGreater(len(info), 1)
        self.assertIn('host', info)
        self.assertIn('os', info)
        self.assertIn('cpu', info)
        self.assertIn('ram', info)
