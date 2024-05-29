import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetMoonriseTime(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_moonrise_time(self):
        date = datetime.datetime(2024, 6, 22)
        moonrise = self.eph.get_moonrise_time(date).strftime('%H:%M:%S')
        self.assertEqual(moonrise, '23:11:04')

if __name__ == '__main__':
    unittest.main()