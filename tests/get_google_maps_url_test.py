import unittest
from context import astrobot
from astrobot import utils

class TestGetGoogleMapsUrl(unittest.TestCase):
    def test_get_google_maps_url(self):
        url = utils.get_google_maps_url(48.8566, 2.3522)
        self.assertEqual(url, 'https://www.google.com/maps/place/48°51′23.8″N+2°21′07.9″E')

if __name__ == '__main__':
    unittest.main()
