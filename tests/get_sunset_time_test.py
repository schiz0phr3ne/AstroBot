import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetSunsetTime(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_sunset_time(self):
        date = datetime.datetime(2024, 6, 22)
        sunset = self.eph.get_sunset_time(date).strftime('%H:%M:%S')
        self.assertEqual(sunset, '21:58:06')

if __name__ == '__main__':
    unittest.main()
