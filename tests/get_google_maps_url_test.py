"""
This file contains the tests for the get_google_maps_url function in the utils module.
The utils module provides utility functions for the AstroBot project.

Attributes:
    None

Methods:
    test_get_google_maps_url: Test the get_google_maps_url function.
"""

import unittest
from context import astrobot
from astrobot import utils

class TestGetGoogleMapsUrl(unittest.TestCase):
    """
    Test the get_google_maps_url function in the utils module.
    
    Attributes:
        None
        
    Methods:
        test_get_google_maps_url: Test the get_google_maps_url function.
    """
    def test_get_google_maps_url(self):
        """
        Test case for the get_google_maps_url function.
        It verifies that the function correctly generates a Google Maps URL
        for a given latitude and longitude.
        """
        url = utils.get_google_maps_url(48.8566, 2.3522)
        self.assertEqual(url, 'https://www.google.com/maps/place/48°51′23.8″N+2°21′07.9″E')

if __name__ == '__main__':
    unittest.main()
