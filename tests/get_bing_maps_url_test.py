import unittest
from context import astrobot
from astrobot import utils

class TestGetBingMapsUrl(unittest.TestCase):
    def test_get_bing_maps_url(self):
        url = utils.get_bing_maps_url(48.8566, 2.3522)
        self.assertEqual(url, 'https://www.bing.com/maps?cp=48.8566~2.3522&lvl=17')

if __name__ == '__main__':
    unittest.main()
