from datetime import datetime
from zoneinfo import ZoneInfo

from skyfield import almanac
from skyfield.api import N, E, load, load_file, Loader, wgs84


class Ephemeris:
    """
    A class to represent an observer's location, and compute ephemeris.
    
    Attributes:
        latitude (float): The latitude of the observer, in decimal notation.
        longitude (float): The longitude of the observer, in decimal notation.
        altitude (float): The altitude of the observer in meters.
        timezone (str): The timezone of the observer.
    
    Methods:
        get_sunrise_time(date): Get the sunrise time for the given date.
        get_sunset_time(date): Get the sunset time for the given date.
        get_moonrise_time(date): Get the moonrise time for the given date.
        get_moonset_time(date): Get the moonset time for the given date.
        get_planet_rising_time(date, planet): Get the rise time for the given planet on the given date.
        get_planet_setting_time(date, planet): Get the set time for the given planet on the given date.
        get_twilight_times(date): Get the start and end times of civil, nautical, and astronomical twilight for the given date.
    """

    def __init__(self, latitude, longitude, altitude, timezone=None):
        """
        Initialize the Ephemeris object.

        Args:
            latitude (float): The latitude of the observer.
            longitude (float): The longitude of the observer.
            altitude (float): The altitude of the observer in meters.
            timezone (str, optional): The timezone of the observer. Defaults to 'UTC'.
        """
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.timezone = ZoneInfo(timezone) if timezone else ZoneInfo('UTC')
        
        # Create an observer object
        self.observer = wgs84.latlon(self.latitude * N, self.longitude * E, elevation_m=self.altitude)

    def get_sunrise_time(self, date):
        """
        Get the sunrise time for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the sunrise time.

        Returns:
            datetime.time: The sunrise time in the local timezone.
        """
        # Add UTC timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.from_datetime(date)
        t1 = ts.from_datetime(date.replace(day=date.day + 1))
        
        # Load the Earth and Sun ephemeris
        try:
            planets = load_file('files/de440s.bsp')
        except FileNotFoundError:
            loader = Loader('files')
            planets = loader('de440s.bsp')
        earth, sun = planets['earth'], planets['sun']

        # Compute the position of the observer
        observer = earth + self.observer

        # Compute the sunrise time
        sunrise_time, _ = almanac.find_risings(observer, sun, t0, t1)
        try:
            sunrise = sunrise_time[0]
        except IndexError:
            return None

        # Adjust the sunrise time to the local timezone
        sunrise = sunrise.astimezone(self.timezone)

        return sunrise.time()

    def get_sunset_time(self, date):
        """
        Get the sunset time for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the sunset time.

        Returns:
            datetime.time: The sunset time in the local timezone.
        """
        # Add UTC timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.from_datetime(date)
        t1 = ts.from_datetime(date.replace(day=date.day + 1))

        # Load the Earth and Sun ephemeris
        try:
            planets = load_file('files/de440s.bsp')
        except FileNotFoundError:
            loader = Loader('files')
            planets = loader('de440s.bsp')
        earth, sun = planets['earth'], planets['sun']

        # Compute the position of the observer
        observer = earth + self.observer
        
        # Compute the sunset time
        sunset_time, _ = almanac.find_settings(observer, sun, t0, t1)
        try:
            sunset = sunset_time[0]
        except IndexError:
            return None
        
        # Adjust the sunset time to the local timezone
        sunset = sunset.astimezone(self.timezone)

        return sunset.time()
    
    def get_moonrise_time(self, date):
        """
        Get the moonrise time for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the moonrise time.

        Returns:
            datetime.time: The moonrise time in the local timezone.
        """
        # Add UTC timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.from_datetime(date)
        t1 = ts.from_datetime(date.replace(day=date.day + 1))

        # Load the Earth and Moon ephemeris
        try:
            planets = load_file('files/de440s.bsp')
        except FileNotFoundError:
            loader = Loader('files')
            planets = loader('de440s.bsp')
        earth, moon = planets['earth'], planets['moon']

        # Compute the position of the observer
        observer = earth + self.observer

        # Compute the moonrise time
        moonrise_time, _ = almanac.find_risings(observer, moon, t0, t1)
        try:
            moonrise = moonrise_time[0]
        except IndexError:
            return None

        # Adjust the moonrise time to the local timezone
        moonrise = moonrise.astimezone(self.timezone)

        return moonrise.time()

    def get_moonset_time(self, date):
        """
        Get the moonset time for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the moonset time.

        Returns:
            datetime.time: The moonset time in the local timezone.
        """
        # Add UTC timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.from_datetime(date)
        t1 = ts.from_datetime(date.replace(day=date.day + 1))

        # Load the Earth and Moon ephemeris
        try:
            planets = load_file('files/de440s.bsp')
        except FileNotFoundError:
            loader = Loader('files')
            planets = loader('de440s.bsp')
        earth, moon = planets['earth'], planets['moon']

        # Compute the position of the observer
        observer = earth + self.observer
        
        # Compute the moonset time
        moonset_time, _ = almanac.find_settings(observer, moon, t0, t1)
        try:
            moonset = moonset_time[0]
        except IndexError:
            return None
        
        # Adjust the moonset time to the local timezone
        moonset = moonset.astimezone(self.timezone)

        return moonset.time()

    def get_planet_rising_time(self, date, planet):
        """
        Get the rise time for the given planet on the given date.

        Args:
            date (datetime.datetime): The date for which to compute the rise time.
            planet (str): The name of the planet for which to compute the rise time.

        Returns:
            datetime.time: The rise time in the local timezone.
        """
        # Add UTC timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.from_datetime(date)
        t1 = ts.from_datetime(date.replace(day=date.day + 1))

        # Load the Earth and planet ephemeris
        try:
            planets = load_file('files/de440s.bsp')
        except FileNotFoundError:
            loader = Loader('files')
            planets = loader('de440s.bsp')
        earth, planet = planets['earth'], planets[f'{planet} barycenter']

        # Compute the position of the observer
        observer = earth + self.observer

        # Compute the rise time
        rise_time, _ = almanac.find_risings(observer, planet, t0, t1)
        try:
            rise = rise_time[0]
        except IndexError:
            return None

        # Adjust the rise time to the local timezone
        rise = rise.astimezone(self.timezone)

        return rise.time()
    
    def get_planet_setting_time(self, date, planet):
        """
        Get the set time for the given planet on the given date.

        Args:
            date (datetime.datetime): The date for which to compute the set time.
            planet (str): The name of the planet for which to compute the set time.

        Returns:
            datetime.time: The set time in the local timezone.
        """
        # Add UTC timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.from_datetime(date)
        t1 = ts.from_datetime(date.replace(day=date.day + 1))

        # Load the Earth and planet ephemeris
        try:
            planets = load_file('files/de440s.bsp')
        except FileNotFoundError:
            loader = Loader('files')
            planets = loader('de440s.bsp')
        earth, planet = planets['earth'], planets[f'{planet} barycenter']

        # Compute the position of the observer
        observer = earth + self.observer
        
        # Compute the set time
        set_time, _ = almanac.find_settings(observer, planet, t0, t1)
        try:
            set = set_time[0]
        except IndexError:
            return None
        
        # Adjust the set time to the local timezone
        set = set.astimezone(self.timezone)

        return set.time()
    
    def get_twilight_times(self, date):
        """
        Get the start and end times of civil, nautical, and astronomical twilight for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the twilight times.

        Returns:
            list: A list of datetime.time objects representing the start and end times of civil, nautical, and astronomical twilight.
        """
        # Add UTC timezone information to the date object, and replace the time with noon
        date = date.replace(hour=12, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create a time object for the given date
        ts = load.timescale()
        t0 = ts.from_datetime(date)
        t1 = ts.from_datetime(date.replace(day=date.day + 1))

        # Load the Earth and Sun ephemeris
        try:
            planets = load_file('files/de440s.bsp')
        except FileNotFoundError:
            loader = Loader('files')
            planets = loader('de440s.bsp')

        # Compute the dark twilight times
        f = almanac.dark_twilight_day(planets, self.observer)
        events, _ = almanac.find_discrete(t0, t1, f)
        
        # Adjust the twilight times to the local timezone
        if events:
            twilight_times = []
            for event in events:
                event = event.astimezone(self.timezone)
                twilight_times.append(event.time())
        else:
            return None
        
        return twilight_times
