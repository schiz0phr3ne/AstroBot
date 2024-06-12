"""
This script tests the get_planet_rise_time method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as planet rise times.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_get_planet_rise_time: Test the get_planet_rise_time method.
"""

import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetPlanetRiseTime(unittest.TestCase):
    """
    Test the get_planet_rise_time method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_get_planet_rise_time: Test the get_planet_rise_time method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_planet_rise_time(self):
        """
        Test case for the get_planet_rise_time method.
        It verifies that the computed planet rise time for a given date matches the expected time.
        """
        date = datetime.datetime(2024, 6, 22)
        planet_rise = self.eph.get_planet_rise_time(date, 'Mars').strftime('%H:%M:%S')
        self.assertEqual(planet_rise, '03:09:01')

if __name__ == '__main__':
    unittest.main()
