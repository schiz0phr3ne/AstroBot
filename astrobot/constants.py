"""
This module contains constants used in the AstroBot application.
"""

ASTROBIN_API_IOTD_URL = 'imageoftheday/?limit=1'
ASTROBIN_API_URL = 'api/v1/'
ASTROBIN_BASE_URL = 'https://astrobin.com'
ASTROBIN_LOGO_URL = 'https://cdn.astrobin.com/static/astrobin/images/astrobin-logo-small.39b63752c38d.png'
ASTROBIN_USERS_URL = 'https://astrobin.com/users/'

BODIES = {
    'sun': ('gold', 25),
    'mercury': ('#b1adad', 10),
    'venus': ('#efe8d8', 15),
    'moon': ('lightgrey', 25),
    'mars': ('#e27b58', 10),
    'jupiter': ('#d8ca9d', 20),
    'saturn': ('#c3924f', 20),
    'uranus': ('#c6d3e3', 15),
    'neptune': ('#274687', 15),
    'pluto': ('peru', 5),
}

DIRECTIONS = ['N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO', '']

NASA_API_APOD_URL = 'https://api.nasa.gov/planetary/apod'
NASA_APOD_URL = 'https://apod.nasa.gov/apod/astropix.html'
NASA_LOGO_URL = 'https://gpm.nasa.gov/sites/default/files/document_files/NASA-Logo-Large.png'

PLANETS = {
    'Mercure': 'mercury',
    'Vénus': 'venus',
    'Mars': 'mars',
    'Jupiter': 'jupiter',
    'Saturne': 'saturn',
    'Uranus': 'uranus',
    'Neptune': 'neptune',
    'Pluton': 'pluto'
}

PLOT_TYPES = {
    'Polaire': 'polar',
    'Cartésien': 'cartesian'
}
