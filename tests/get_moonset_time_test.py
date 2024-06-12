"""
This script tests the get_moonset_time method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as moonset times.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_get_moonset_time: Test the get_moonset_time method.
"""

import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetMoonsetTime(unittest.TestCase):
    """
    Test the get_moonset_time method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_get_moonset_time: Test the get_moonset_time method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_moonset_time(self):
        """
        Test case for the get_moonset_time method.
        It verifies that the computed moonset time for a given date matches the expected time.
        """
        date = datetime.datetime(2024, 6, 22)
        moonset = self.eph.get_moonset_time(date).strftime('%H:%M:%S')
        self.assertEqual(moonset, '05:24:30')

if __name__ == '__main__':
    unittest.main()
