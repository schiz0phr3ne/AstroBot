"""
This script tests the get_sunset_time method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as sunset times.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_get_sunset_time: Test the get_sunset_time method.
"""

import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetSunsetTime(unittest.TestCase):
    """
    Test the get_sunset_time method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_get_sunset_time: Test the get_sunset_time method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_sunset_time(self):
        """
        Test case for the get_sunset_time method.
        It verifies that the computed sunset time for a given date matches the expected time.
        """
        date = datetime.datetime(2024, 6, 22)
        sunset = self.eph.get_sunset_time(date).strftime('%H:%M:%S')
        self.assertEqual(sunset, '21:58:06')

if __name__ == '__main__':
    unittest.main()
