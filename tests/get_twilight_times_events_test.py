import datetime
import unittest
from context import astrobot
from astrobot import ephemeris

class TestGetTwilightTimesEvents(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_get_twilight_times_event(self):
        date = datetime.datetime(2024, 6, 22)
        twilight_times, twilight_events = self.eph.get_twilight_times_events(date)
        twilight_times = [twilight_time.strftime('%H:%M:%S') for twilight_time in twilight_times]
        self.assertEqual(twilight_times, ['21:58:06', '22:40:45', '23:41:27', '04:04:14', '05:04:56', '05:47:35'])
        for pair in zip(twilight_events, [3, 2, 1, 2, 3, 4]):
            self.assertEqual(pair[0], pair[1])

if __name__ == '__main__':
    unittest.main()