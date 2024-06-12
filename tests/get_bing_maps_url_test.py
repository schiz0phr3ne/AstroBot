"""
This script tests the get_bing_maps_url function in the utils module.
The utils module provides utility functions for the AstroBot project.

Attributes:
    None

Methods:
    test_get_bing_maps_url: Test the get_bing_maps_url function.
"""

import unittest
from context import astrobot
from astrobot import utils

class TestGetBingMapsUrl(unittest.TestCase):
    """
    Test the get_bing_maps_url function in the utils module.
    
    Attributes:
        None
    
    Methods:
        test_get_bing_maps_url: Test the get_bing_maps_url function.
    """
    def test_get_bing_maps_url(self):
        """
        Test case for the get_bing_maps_url function.
        It verifies that the function correctly generates a Bing Maps URL
        for a given latitude and longitude.
        """
        url = utils.get_bing_maps_url(48.8566, 2.3522)
        self.assertEqual(url, 'https://www.bing.com/maps?cp=48.8566~2.3522&lvl=17')

if __name__ == '__main__':
    unittest.main()
