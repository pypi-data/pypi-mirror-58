"""
Tests for `zelos packaging`.
"""

import zelos


class TestTest(object):
    """
    Tests for `optional`.
    """

    def test_equal(self):
        """
        Test equal comparator.
        """
        z = zelos.Engine()
        z.start()
        assert 42 == 42

    def test_not_equal(self):
        """
        Test not equal comparator.
        """
        z = zelos.Engine()
        z.start()
        assert 24 != 42
