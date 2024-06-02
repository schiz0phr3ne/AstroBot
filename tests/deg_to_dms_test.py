import unittest
from context import astrobot
from astrobot import utils

class TestDegToDms(unittest.TestCase):
    def test_deg_to_dms(self):
        dms = utils.deg_to_dms(48.8566)
        self.assertEqual(dms, '48°51′23.8″')

if __name__ == '__main__':
    unittest.main()