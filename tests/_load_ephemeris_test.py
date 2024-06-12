"""
This module contains a unit test for the load_ephemeris method of the Ephemeris class.
The Ephemeris class provides methods to calculate astronomical events such as solstices.

Attributes:
    None

Methods:
    setUp: Initialize the Ephemeris object.
    test_load_ephemeris: Test the load_ephemeris method.
"""
import unittest
from context import astrobot
from astrobot import ephemeris

class TestLoadEphemeris(unittest.TestCase):
    """
    Test the load_ephemeris method of the Ephemeris class.
    
    Attributes:
        eph (Ephemeris): The Ephemeris object.
    
    Methods:
        setUp: Initialize the Ephemeris object.
        test_load_ephemeris: Test the load_ephemeris method.
    """
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_load_ephemeris(self):
        """
        Test case for the load_ephemeris method.
        
        This method tests the load_ephemeris method of the Ephemeris class.
        It verifies that the ephemeris file is loaded correctly and the path is set.
        """
        filename = 'de440s.bsp'
        eph = self.eph._load_ephemeris(filename)
        self.assertEqual(eph.path, f'files/{filename}')

if __name__ == '__main__':
    unittest.main()