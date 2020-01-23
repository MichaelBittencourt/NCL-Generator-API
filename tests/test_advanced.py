# -*- coding: utf-8 -*-

from .context import ncl

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNotNone(ncl.Ncl())


if __name__ == '__main__':
    unittest.main()
