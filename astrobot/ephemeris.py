from zoneinfo import ZoneInfo

from datetime import timedelta
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
        _load_ephemeris(filename): Load the ephemeris file.
        _set_time_range(date): Set the time range for the given date.
        get_sunrise_time(date): Get the sunrise time for the given date.
        get_sunset_time(date): Get the sunset time for the given date.
        get_moonrise_time(date): Get the moonrise time for the given date.
        get_moonset_time(date): Get the moonset time for the given date.
        get_moon_phase(date): Get the moon phase for the given date.
        get_planet_rising_time(date, planet): Get the rise time for the given planet on the given date.
        get_planet_setting_time(date, planet): Get the set time for the given planet on the given date.
        get_twilight_times_events(date): Get the start and end times of civil, nautical, and astronomical twilight for the given date.
    """

    def __init__(
        self,
        latitude,
        longitude,
        altitude,
        timezone=None
    ):
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
    
    def _load_ephemeris(
        self,
        filename
    ):
        """
        Load the ephemeris file.

        Args:
            filename (str): The name of the ephemeris file.

        Returns:
            skyfield.api.Loader: The ephemeris object.
        """
        try:
            eph = load_file(f'files/{filename}')
        except FileNotFoundError:
            loader = Loader('files')
            eph = loader(filename)
        
        return eph

    def _set_time_range(
        self,
        date
    ):
        """
        Set the time range for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the ephemeris.

        Returns:
            tuple: A tuple containing the start and end times of the time range.
        """
        ts = load.timescale()
        t0 = ts.from_datetime(date)
        t1 = ts.from_datetime(date + timedelta(days=1))
        
        return t0, t1

    def get_sunrise_time(
        self,
        date
    ):
        """
        Get the sunrise time for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the sunrise time.

        Returns:
            datetime.time: The sunrise time in the local timezone.
        """
        # Add timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create time range
        t0, t1 = self._set_time_range(date)
        
        # Load  ephemeris
        eph = self._load_ephemeris('de440s.bsp')
        earth, sun = eph['earth'], eph['sun']

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

    def get_sunset_time(
        self,
        date
    ):
        """
        Get the sunset time for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the sunset time.

        Returns:
            datetime.time: The sunset time in the local timezone.
        """
        # Add timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create time range
        t0, t1 = self._set_time_range(date)

        # Load  ephemeris
        eph = self._load_ephemeris('de440s.bsp')
        earth, sun = eph['earth'], eph['sun']

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
    
    def get_moonrise_time(
        self,
        date
    ):
        """
        Get the moonrise time for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the moonrise time.

        Returns:
            datetime.time: The moonrise time in the local timezone.
        """
        # Add timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create time range
        t0, t1 = self._set_time_range(date)

        # Load  ephemeris
        eph = self._load_ephemeris('de440s.bsp')
        earth, moon = eph['earth'], eph['moon']

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

    def get_moonset_time(
        self,
        date
    ):
        """
        Get the moonset time for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the moonset time.

        Returns:
            datetime.time: The moonset time in the local timezone.
        """
        # Add timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create time range
        t0, t1 = self._set_time_range(date)

        # Load  ephemeris
        eph = self._load_ephemeris('de440s.bsp')
        earth, moon = eph['earth'], eph['moon']

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
    
    def get_moon_phase(
        self,
        date
    ):
        """
        Get the moon phase for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the moon phase.

        Returns:
            float: The moon phase in degrees.
        """
        # Add timezone information to the date object, and replace the time with noon
        date = date.replace(hour=12, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create the time object for the given date
        t0, _ = self._set_time_range(date)
        
        # Load  ephemeris
        eph = self._load_ephemeris('de440s.bsp')
        
        # Compute the moon phase
        phase = almanac.moon_phase(eph, t0)
        
        return phase.degrees

    def get_planet_rise_time(
        self,
        date,
        planet
    ):
        """
        Get the rise time for the given planet on the given date.

        Args:
            date (datetime.datetime): The date for which to compute the rise time.
            planet (str): The name of the planet for which to compute the rise time.

        Returns:
            datetime.time: The rise time in the local timezone.
        """
        # Add timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create time range
        t0, t1 = self._set_time_range(date)

        # Load  ephemeris
        eph = self._load_ephemeris('de440s.bsp')
        earth, planet = eph['earth'], eph[f'{planet} barycenter']

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
    
    def get_planet_set_time(
        self,
        date,
        planet
    ):
        """
        Get the set time for the given planet on the given date.

        Args:
            date (datetime.datetime): The date for which to compute the set time.
            planet (str): The name of the planet for which to compute the set time.

        Returns:
            datetime.time: The set time in the local timezone.
        """
        # Add timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create time range
        t0, t1 = self._set_time_range(date)

        # Load  ephemeris
        eph = self._load_ephemeris('de440s.bsp')
        earth, planet = eph['earth'], eph[f'{planet} barycenter']

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
    
    def get_twilight_times_events(
        self,
        date
    ):
        """
        Get the start and end times of civil, nautical, and astronomical twilight for the given date.

        Args:
            date (datetime.datetime): The date for which to compute the twilight times.

        Returns:
            tuple: A tuple containing the twilight times and events in the local timezone.
        """
        # Add timezone information to the date object, and replace the time with noon
        date = date.replace(hour=12, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create time range
        t0, t1 = self._set_time_range(date)

        # Load  ephemeris
        eph = self._load_ephemeris('de440s.bsp')

        # Compute the dark twilight times
        f = almanac.dark_twilight_day(eph, self.observer)
        times, twilight_events = almanac.find_discrete(t0, t1, f)
        
        # Adjust the twilight times to the local timezone
        if times:
            twilight_times = []
            for time in times:
                time = time.astimezone(self.timezone)
                twilight_times.append(time.time())
        else:
            return None
        
        return twilight_times, twilight_events

    def compute_position(
        self,
        date,
        object,
    ):
        """
        Compute the position of the given object on the given date.

        Args:
            date (datetime.datetime): The date for which to compute the position.
            object (str): The name of the object for which to compute the position.

        Returns:
            tuple: A tuple containing the altitude and azimuth of the object.
        """
        # Add timezone information to the date object, and replace the time with noon
        date = date.replace(hour=12, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create the time object for the given date
        t0, _ = self._set_time_range(date)
        
        # Load  ephemeris
        eph = self._load_ephemeris('de440s.bsp')
        
        # Compute the position of the object
        earth, obj = eph['earth'], eph[object]
        observer = earth + self.observer
        alt, az, _ = observer.at(t0).observe(obj).apparent().altaz()
        
        return alt.degrees, az.degrees
    
    def compute_daily_path(
        self,
        date,
        object,
        delta=timedelta(minutes=20)
    ):
        """
        Compute the daily path of the given object on the given date.
        
        Args:
            object (str): The name of the object for which to compute the path.
            date (datetime.datetime): The date for which to compute the path.
            delta (timedelta, optional): The time interval between each position. Defaults to 20 minutes.
        
        Returns:
            tuple: A tuple containing the altitude and azimuth of the object at each interval.
        """
        # Add timezone information to the date object, and replace the time with midnight
        date = date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=self.timezone)
        
        # Create the time object for the given date
        t0, t1 = self._set_time_range(date)
        
        # Load  ephemeris
        eph = self._load_ephemeris('de440s.bsp')
        
        # Compute the position of the object at each interval
        earth, obj = eph['earth'], eph[object]
        observer = earth + self.observer
        altitudes, azimuths = [], []
        for interval in range(24 * 3 + 1):
            t = t0 + delta * interval
            alt, az, _ = observer.at(t).observe(obj).apparent().altaz()
            altitudes.append(round(alt.degrees, 2))
            azimuths.append(round(az.degrees, 2))
        
        return altitudes, azimuths