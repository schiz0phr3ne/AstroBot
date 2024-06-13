"""
This script contains a unit test for the get_seasons method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as seasons.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_get_seasons: Test the get_season method.
"""

import datetime
import unittest

from context import astrobot
from astrobot import ephemeris

class TestGetSeason(unittest.TestCase):
    """
    Test the get_season method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_get_season: Test the get_season method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_seasons(self):
        """
        Test case for the get_season method.

        This method tests the get_seasons method of the Ephemeris class.
        It verifies that the computed season for a given date matches the expected season.
        """
        year = 2024
        seasons_date, seasons_name = self.eph.get_seasons(year)
        self.assertEqual(seasons_date[1].date(), datetime.date(2024, 6, 20))
        self.assertEqual(seasons_name[1], 'summer')

if __name__ == '__main__':
    unittest.main()
