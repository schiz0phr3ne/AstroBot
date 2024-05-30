import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestLoadEphemeris(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_load_ephemeris(self):
        filename = 'de440s.bsp'
        eph = self.eph._load_ephemeris(filename)
        self.assertEqual(eph.path, f'files/{filename}')

if __name__ == '__main__':
    unittest.main()