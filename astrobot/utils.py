from skyfield.api import Angle

def deg_to_dms(
    deg: float
) -> str:
    """
    Convert decimal degrees to degrees, minutes and seconds.

    Args:
        deg (float): The decimal degree to convert.

    Returns:
        str: The degrees, minutes and seconds formatted as a string.
    """
    return Angle(degrees=deg).dstr(format=u'{0}{1}°{2:02}′{3:02}.{4:0{5}}″')

def get_bing_maps_url(
    latitude: float,
    longitude: float
) -> str:
    """
    Get a Bing Maps URL for a given latitude and longitude.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.

    Returns:
        str: The Bing Maps URL.
    """
    return f'https://www.bing.com/maps?cp={latitude}~{longitude}&lvl=17'

def get_google_maps_url(
    latitude: float,
    longitude: float
) -> str:
    """
    Get a Google Maps URL for a given latitude and longitude.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.

    Returns:
        str: The Google Maps URL.
    """
    latitude_dms = deg_to_dms(latitude)
    longitude_dms = deg_to_dms(longitude)
    latitude_position = 'N' if latitude >= 0 else 'S'
    longitude_position = 'E' if longitude >= 0 else 'W'
    return f'https://www.google.com/maps/place/{latitude_dms}{latitude_position}+{longitude_dms}{longitude_position}'
