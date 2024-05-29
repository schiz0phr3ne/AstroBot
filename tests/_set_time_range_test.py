import unittest
from datetime import datetime, timedelta
from context import astrobot
from astrobot import ephemeris

class TestSetTimeRange(unittest.TestCase):
    def setUp(self):
        self.eph = ephemeris.Ephemeris(48.8566, 2.3522, 0, 'Europe/Paris')

    def test_set_time_range(self):
        start = datetime.now(tz=self.eph.timezone)
        end = start + timedelta(days=1)
        t0, t1 = self.eph._set_time_range(start)
        t0 = t0.astimezone(self.eph.timezone)
        t1 = t1.astimezone(self.eph.timezone)

        self.assertEqual(t0, start)
        self.assertEqual(t1, end)

if __name__ == '__main__':
    unittest.main()