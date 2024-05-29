import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetSunriseTime(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_sunrise_time(self):
        date = datetime.datetime(2024, 6, 22)
        sunrise = self.eph.get_sunrise_time(date).strftime('%H:%M:%S')
        self.assertEqual(sunrise, '05:47:18')

if __name__ == '__main__':
    unittest.main()
