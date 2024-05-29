import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetPlanetSetTime(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_planet_set_time(self):
        date = datetime.datetime(2024, 6, 22)
        planet_set = self.eph.get_planet_set_time(date, 'Mars').strftime('%H:%M:%S')
        self.assertEqual(planet_set, '17:25:46')

if __name__ == '__main__':
    unittest.main()