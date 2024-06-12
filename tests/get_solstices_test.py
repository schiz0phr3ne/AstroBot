import datetime
import unittest

from context import astrobot
from astrobot import ephemeris

class TestGetSolstice(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_solstice(self):
        date = datetime.datetime(2024, 6, 22)
        summer_solstice, winter_solstice = self.eph.get_solstices(date)
        self.assertEqual(summer_solstice, datetime.date(2024, 6, 20))
        self.assertEqual(winter_solstice, datetime.date(2024, 12, 21))

if __name__ == '__main__':
    unittest.main()
