import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetMoonsetTime(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_moonset_time(self):
        date = datetime.datetime(2024, 6, 22)
        moonset = self.eph.get_moonset_time(date).strftime('%H:%M:%S')
        self.assertEqual(moonset, '05:24:30')

if __name__ == '__main__':
    unittest.main()
