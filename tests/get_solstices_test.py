"""
This module contains a unit test for the get_solstice method of the Ephemeris class.

The Ephemeris class provides methods to calculate astronomical events such as solstices.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_get_solstice: Test the get_solstice method.
"""

import datetime
import unittest

from context import astrobot
from astrobot import ephemeris

class TestGetSolstice(unittest.TestCase):
    """
    Test the get_solstice method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_get_solstice: Test the get_solstice method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_solstice(self):
        """
        Test the get_solstice method.
        """
        year = 2024
        summer_solstice, winter_solstice = self.eph.get_solstices(year)
        self.assertEqual(summer_solstice.date(), datetime.date(2024, 6, 20))
        self.assertEqual(winter_solstice.date(), datetime.date(2024, 12, 21))

if __name__ == '__main__':
    unittest.main()
