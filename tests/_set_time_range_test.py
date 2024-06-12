"""
Test the _set_time_range method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as solstices.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_set_time_range: Test the _set_time_range method.
"""

import unittest
from datetime import datetime, timedelta
from context import astrobot
from astrobot import ephemeris

class TestSetTimeRange(unittest.TestCase):
    """
    Test the _set_time_range method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_set_time_range: Test the _set_time_range method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_set_time_range(self):
        """
        Test case for the _set_time_range method.
        """
        start = datetime.now(tz=self.eph.timezone)
        end = start + timedelta(days=1)
        t0, t1 = self.eph._set_time_range(start)
        t0 = t0.astimezone(self.eph.timezone)
        t1 = t1.astimezone(self.eph.timezone)

        self.assertEqual(t0, start)
        self.assertEqual(t1, end)

if __name__ == '__main__':
    unittest.main()
