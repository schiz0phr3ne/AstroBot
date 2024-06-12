"""
This module contains the tests for the get_moon_phase method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as moon phases.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_get_moon_phase: Test the get_moon_phase method.
"""

import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetMoonPhase(unittest.TestCase):
    """
    Test the get_moon_phase method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_get_moon_phase: Test the get_moon_phase method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_moon_phase(self):
        """
        Test case for the get_moon_phase method.
        It verifies that the computed moon phase for a given date matches the expected value.
        """
        # Test for a full moon
        date1 = datetime.datetime(2024, 6, 22)
        phase1 = self.eph.get_moon_phase(date1)
        self.assertAlmostEqual(phase1, 180.0, delta=10)

        # Test for a new moon
        date2 = datetime.datetime(2024, 6, 6)
        phase2 = self.eph.get_moon_phase(date2)
        if phase2 < 180:
            self.assertAlmostEqual(phase2, 0.0, delta=10)
        else:
            self.assertAlmostEqual(phase2, 360.0, delta=10)

        # Test for a first quarter moon
        date3 = datetime.datetime(2024, 5, 15)
        phase3 = self.eph.get_moon_phase(date3)
        self.assertAlmostEqual(phase3, 90, delta=10)

        # Test for a last quarter moon
        date4 = datetime.datetime(2024, 5, 30)
        phase4 = self.eph.get_moon_phase(date4)
        self.assertAlmostEqual(phase4, 270, delta=10)

if __name__ == '__main__':
    unittest.main()
