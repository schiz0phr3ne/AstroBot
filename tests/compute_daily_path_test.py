"""
Test the compute_daily_path method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as solstices.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_compute_daily_path: Test the compute_daily_path method.
"""

import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestComputeDailyPath(unittest.TestCase):
    """
    Test the compute_daily_path method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_compute_daily_path: Test the compute_daily_path method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_compute_daily_path(self):
        """
        Test case for the compute_daily_path method.
        It verifies that the computed azimuth and altitude values for a given date and celestial
        object match the expected values with a specified decimal place precision.
        """
        date = datetime.datetime(2024, 6, 22, 0, 0, 0)
        daily_path = self.eph.compute_daily_path(date, 'sun')
        self.assertEqual(len(daily_path[0]), 24*3+1)
        self.assertEqual(daily_path[0][18], 0.83)
        self.assertEqual(daily_path[1][18], 54.0)

if __name__ == '__main__':
    unittest.main()
