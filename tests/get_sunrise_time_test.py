"""
This script contains a unit test for the get_sunrise_time method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as sunrise times.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_get_sunrise_time: Test the get_sunrise_time method.
"""

import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetSunriseTime(unittest.TestCase):
    """
    Test the get_sunrise_time method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_get_sunrise_time: Test the get_sunrise_time method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_sunrise_time(self):
        """
        Test case for the get_sunrise_time method.
        It verifies that the computed sunrise time for a given date matches the expected time.
        """
        date = datetime.datetime(2024, 6, 22)
        sunrise = self.eph.get_sunrise_time(date).strftime('%H:%M:%S')
        self.assertEqual(sunrise, '05:47:18')

if __name__ == '__main__':
    unittest.main()
