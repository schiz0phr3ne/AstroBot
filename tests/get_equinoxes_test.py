"""
This script contains a unit test for the get_equinox method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as equinoxes.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_get_equinox: Test the get_equinox method.
"""

import datetime
import unittest

from context import astrobot
from astrobot import ephemeris

class TestGetEquinox(unittest.TestCase):
    """
    Test the get_equinox method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_get_equinox: Test the get_equinox method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_equinox(self):
        """
        Test case for the get_equinox method.

        This method tests the get_equinox method of the Ephemeris class.
        It verifies that the computed equinox dates for a given year match the expected dates.
        """
        year = 2024
        spring_equinox, autumn_equinox = self.eph.get_equinoxes(year)
        self.assertEqual(spring_equinox.date(), datetime.date(2024, 3, 20))
        self.assertEqual(autumn_equinox.date(), datetime.date(2024, 9, 22))

if __name__ == '__main__':
    unittest.main()
