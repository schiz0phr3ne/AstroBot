import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestComputeDailyPath(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_compute_daily_path(self):
        date = datetime.datetime(2024, 6, 22, 0, 0, 0)
        daily_path = self.eph.compute_daily_path(date, 'sun')
        self.assertEqual(len(daily_path[0]), 24*3+1)
        self.assertEqual(daily_path[0][18], 0.83)
        self.assertEqual(daily_path[1][18], 54.0)

if __name__ == '__main__':
    unittest.main()