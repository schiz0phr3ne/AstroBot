"""
Test for the deg_to_dms function in the utils module.
The utils module provides utility functions for the AstroBot application.

Attributes:
    None

Methods:
    test_deg_to_dms: Test the deg_to_dms function.
"""

import unittest
from context import astrobot
from astrobot import utils

class TestDegToDms(unittest.TestCase):
    """
    Test the deg_to_dms function in the utils module.
    
    Attributes:
        None
    
    Methods:
        test_deg_to_dms: Test the deg_to_dms function.
    """
    def test_deg_to_dms(self):
        """
        Test case for the deg_to_dms function.
        It verifies that the function correctly converts decimal degrees to degrees,
        minutes, and seconds.
        """
        dms = utils.deg_to_dms(48.8566)
        self.assertEqual(dms, '48°51′23.8″')

if __name__ == '__main__':
    unittest.main()
