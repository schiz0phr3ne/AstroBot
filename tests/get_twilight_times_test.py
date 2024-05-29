import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetTwilightTimes(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_twilight_times(self):
        date = datetime.datetime(2024, 6, 22)
        twilight_times = self.eph.get_twilight_times(date)
        twilight_times = [twilight_time.strftime('%H:%M:%S') for twilight_time in twilight_times]
        self.assertEqual(twilight_times, ['21:58:06', '22:40:45', '23:41:27', '04:04:14', '05:04:56', '05:47:35'])

if __name__ == '__main__':
    unittest.main()