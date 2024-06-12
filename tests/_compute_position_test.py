"""
This module contains a unit test for the compute_position method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as solstices.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_compute_position: Test the compute_position method.
"""

import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestComputePosition(unittest.TestCase):
    """
    Test the compute_position method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_compute_position: Test the compute_position method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_compute_position(self):
        """
        Test case for the _compute_position method.

        This method tests the _compute_position method of the AstroBot class.
        It verifies that the computed azimuth and altitude values for a given date and celestial
        object match the expected values with a specified decimal place precision.
        """
        date = datetime.datetime(2024, 6, 22, 12, 0, 0, tzinfo=self.eph.timezone)
        eph = self.eph._load_ephemeris('de440s.bsp')
        az, alt = self.eph._compute_position(date, 'sun', eph)
        decimal_place = 1
        self.assertAlmostEqual(az, 56.26, decimal_place)
        self.assertAlmostEqual(alt, 128.72, decimal_place)

if __name__ == '__main__':
    unittest.main()
