import datetime
from zoneinfo import ZoneInfo

import tzdata
from skyfield import almanac
from skyfield.api import E, Loader, N, S, W, load, wgs84


class Ephemeris:
    """
    A class to represent an observer's location, and compute ephemeris.
    
    Attributes:
        latitude (float): The latitude of the observer.
        longitude (float): The longitude of the observer.
        altitude (float): The altitude of the observer in meters.
        date (datetime.date): The date for which to compute the ephemeris.
        timezone (str): The timezone of the observer.
    
    Methods:
        get_sunrise_time(date): Get the sunrise time for the given date.
        get_sunset_time(date): Get the sunset time for the given date.
        get_moonrise_time(date): Get the moonrise time for the given date.
        get_moonset_time(date): Get the moonset time for the given date.
    """

    def __init__(self, latitude, longitude, altitude, date=None, timezone=None):
        """
        Initialize the Ephemeris object.

        Args:
            latitude (float): The latitude of the observer.
            longitude (float): The longitude of the observer.
            altitude (float): The altitude of the observer in meters.
            date (datetime.date, optional): The date for which to compute the ephemeris. Defaults to today's date.
            timezone (str, optional): The timezone of the observer. Defaults to 'UTC'.
        """
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.date = date if date else datetime.date.today()
        self.timezone = ZoneInfo(timezone) if timezone else ZoneInfo('UTC')
        
        if self.latitude < 0:
            lat = self.latitude * S
        else:
            lat = self.latitude * N
        if self.longitude < 0:
            lon = self.longitude * W
        else:
            lon = self.longitude * E
            
        self.observer = wgs84.latlon(lat, lon, elevation_m=self.altitude)

    def get_sunrise_time(self, date):
        """
        Get the sunrise time for the given date.

        Args:
            date (datetime.date): The date for which to compute the sunrise time.

        Returns:
            datetime.time: The sunrise time in the local timezone.
        """
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.utc(date.year, date.month, date.day)
        t1 = ts.utc(date.year, date.month, date.day + 1)

        # Load the Earth and Sun ephemeris
        loader = Loader('../files')
        planets = load('de421.bsp')
        earth, sun = planets['earth'], planets['sun']

        # Compute the position of the observer
        observer = earth + self.observer

        # Compute the sunrise time
        sunrise_time, _ = almanac.find_risings(observer, sun, t0, t1)
        sunrise = sunrise_time[0]

        # Adjust the sunrise time to the local timezone
        sunrise = sunrise.astimezone(self.timezone)

        return sunrise.time()

    def get_sunset_time(self, date):
        """
        Get the sunset time for the given date.

        Args:
            date (datetime.date): The date for which to compute the sunset time.

        Returns:
            datetime.time: The sunset time in the local timezone.
        """
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.utc(date.year, date.month, date.day)
        t1 = ts.utc(date.year, date.month, date.day + 1)

        # Load the Earth and Sun ephemeris
        loader = Loader('../files')
        planets = load('de421.bsp')
        earth, sun = planets['earth'], planets['sun']

        # Compute the position of the observer
        observer = earth + self.observer
        
        # Compute the sunset time
        sunset_time, _ = almanac.find_settings(observer, sun, t0, t1)
        sunset = sunset_time[0]
        
        # Adjust the sunset time to the local timezone
        sunset = sunset.astimezone(self.timezone)

        return sunset.time()
    
    def get_moonrise_time(self, date):
        """
        Get the moonrise time for the given date.

        Args:
            date (datetime.date): The date for which to compute the moonrise time.

        Returns:
            datetime.time: The moonrise time in the local timezone.
        """
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.utc(date.year, date.month, date.day)
        t1 = ts.utc(date.year, date.month, date.day + 1)

        # Load the Earth and Moon ephemeris
        loader = Loader('../files')
        planets = load('de421.bsp')
        earth, moon = planets['earth'], planets['moon']

        # Compute the position of the observer
        observer = earth + self.observer

        # Compute the moonrise time
        moonrise_time, _ = almanac.find_risings(observer, moon, t0, t1)
        moonrise = moonrise_time[0]

        # Adjust the moonrise time to the local timezone
        moonrise = moonrise.astimezone(self.timezone)

        return moonrise.time()

    def get_moonset_time(self, date):
        """
        Get the moonset time for the given date.

        Args:
            date (datetime.date): The date for which to compute the moonset time.

        Returns:
            datetime.time: The moonset time in the local timezone.
        """
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.utc(date.year, date.month, date.day)
        t1 = ts.utc(date.year, date.month, date.day + 1)

        # Load the Earth and Moon ephemeris
        loader = Loader('../files')
        planets = load('de421.bsp')
        earth, moon = planets['earth'], planets['moon']

        # Compute the position of the observer
        observer = earth + self.observer
        
        # Compute the moonset time
        moonset_time, _ = almanac.find_settings(observer, moon, t0, t1)
        moonset = moonset_time[0]
        
        # Adjust the moonset time to the local timezone
        moonset = moonset.astimezone(self.timezone)

        return moonset.time()

    def get_planet_rising_time(self, date, planet):
        """
        Get the rise time for the given planet on the given date.

        Args:
            date (datetime.date): The date for which to compute the rise time.
            planet (str): The name of the planet for which to compute the rise time.

        Returns:
            datetime.time: The rise time in the local timezone.
        """
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.utc(date.year, date.month, date.day)
        t1 = ts.utc(date.year, date.month, date.day + 1)

        # Load the Earth and planet ephemeris
        loader = Loader('../files')
        planets = load('de421.bsp')
        earth, planet = planets['earth'], planets[planet]

        # Compute the position of the observer
        observer = earth + self.observer

        # Compute the rise time
        rise_time, _ = almanac.find_risings(observer, planet, t0, t1)
        rise = rise_time[0]

        # Adjust the rise time to the local timezone
        rise = rise.astimezone(self.timezone)

        return rise.time()
    
    def get_planet_setting_time(self, date, planet):
        """
        Get the set time for the given planet on the given date.

        Args:
            date (datetime.date): The date for which to compute the set time.
            planet (str): The name of the planet for which to compute the set time.

        Returns:
            datetime.time: The set time in the local timezone.
        """
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.utc(date.year, date.month, date.day)
        t1 = ts.utc(date.year, date.month, date.day + 1)

        # Load the Earth and planet ephemeris
        loader = Loader('../files')
        planets = load('de421.bsp')
        earth, planet = planets['earth'], planets[planet]

        # Compute the position of the observer
        observer = earth + self.observer
        
        # Compute the set time
        set_time, _ = almanac.find_settings(observer, planet, t0, t1)
        set = set_time[0]
        
        # Adjust the set time to the local timezone
        set = set.astimezone(self.timezone)

        return set.time()