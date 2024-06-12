"""
This script tests the get_twilight_times_events method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as twilight times.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_get_twilight_times_event: Test the get_twilight_times_events method.
"""

import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetTwilightTimesEvents(unittest.TestCase):
    """
    Test the get_twilight_times_events method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_get_twilight_times_event: Test the get_twilight_times_events method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_twilight_times_event(self):
        """
        Test case for the get_twilight_times_events method.
        It verifies that the computed twilight times and events for a given date match the
        expected values.
        """
        date = datetime.datetime(2024, 6, 22)
        twilight_times, twilight_events = self.eph.get_twilight_times_events(date)
        twilight_times = [twilight_time.strftime('%H:%M:%S') for twilight_time in twilight_times]
        self.assertEqual(twilight_times, ['21:58:06', '22:40:45', '23:41:27', '04:04:14', '05:04:56', '05:47:35'])
        for pair in zip(twilight_events, [3, 2, 1, 2, 3, 4]):
            self.assertEqual(pair[0], pair[1])

if __name__ == '__main__':
    unittest.main()
