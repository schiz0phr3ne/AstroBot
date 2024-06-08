import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestComputePosition(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_compute_position(self):
        date = datetime.datetime(2024, 6, 22, 12, 0, 0)
        az, alt = self.eph.compute_position(date, 'sun')
        decimal_place = 1
        self.assertAlmostEqual(az, 56.26, decimal_place)
        self.assertAlmostEqual(alt, 128.72, decimal_place)
        
if __name__ == '__main__':
    unittest.main()