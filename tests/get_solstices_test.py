import datetime
import unittest

from context import astrobot
from astrobot import ephemeris

class TestGetSolstice(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_solstice(self):
        year = 2024
        summer_solstice, winter_solstice = self.eph.get_solstices(year)
        self.assertEqual(summer_solstice.date(), datetime.date(2024, 6, 20))
        self.assertEqual(winter_solstice.date(), datetime.date(2024, 12, 21))

if __name__ == '__main__':
    unittest.main()
