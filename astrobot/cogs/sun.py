"""
This module contains the Sun cog for AstroBot.

The Sun cog provides a command to get sunrise and sunset times for a given location and date.

Attributes:
    bot (commands.Bot): The bot instance.

Methods:
    sun: Get sunrise and sunset times for a given location and date.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime

import discord
from discord import Embed, File, Option
from discord.ext import commands

from ephemeris import Ephemeris
from constants import PLOT_TYPES
import plots
import utils

class Sun(commands.Cog):
    """
    Sun cog for AstroBot.
    
    This cog provides a command to get sunrise and sunset times for a given location and date.
    
    Attributes:
        bot (commands.Bot): The bot instance.
    
    Methods:
        sun: Get sunrise and sunset times for a given location and date.
    """
    def __init__(
        self,
        bot
    ):
        self.bot = bot

    @discord.slash_command(description='Get sunrise and sunset times for a given location and date')
    async def sun(
        self,
        ctx,
        latitude: Option(float, description='Latitude of the location'),
        longitude: Option(float, description='Longitude of the location'),
        altitude: Option(int, default=0, description='Altitude of the location'),
        plot_type: Option(str, choices=PLOT_TYPES.keys(), default='Polaire', description='Type of plot (default: polar sky)'),
        day: Option(int, default=0, min_value=1, max_value=31, description='Day of the month (default: today)'),
        month: Option(int, default=0, min_value=1, max_value=12, description='Month of the year (default: this month)'),
        year: Option(int, default=0, min_value=1550, max_value=2650, description='Year (default: this year)')
    ):
        """
        Get sunrise and sunset times for a given location and date.
        
        Args:
            latitude (float): The latitude of the location.
            longitude (float): The longitude of the location.
            altitude (int): The altitude of the location.
            day (int): The day of the month (default: today).
            month (int): The month of the year (default: this month).
            year (int): The year (default: this year).

        Usage:
            /sun latitude longitude altitude day month year

        Example:
            /sun 48.8566 2.3522 0 22 6 2024

        Returns:
            None
        """
        await ctx.defer() # Defer the response to avoid the "This interaction failed" error

        eph = Ephemeris(latitude, longitude, altitude, 'Europe/Paris')

        if day != 0 or month != 0 or year != 0:
            custom_date = True
        else:
            custom_date = False

        # Get the current date if no date is provided
        current_datetime = datetime.now()
        day = current_datetime.day if day == 0 else day
        month = current_datetime.month if month == 0 else month
        year = current_datetime.year if year == 0 else year

        # Get sunrise and sunset times
        sunrise = eph.get_sunrise_time(datetime(year, month, day))
        sunset = eph.get_sunset_time(datetime(year, month, day))

        google_maps_url = utils.get_google_maps_url(latitude, longitude)
        bing_maps_url = utils.get_bing_maps_url(latitude, longitude)

        # If the date is not the actual, compute the polar sky map for the custom date (at midnight)
        if not custom_date:
            compute_datetime = current_datetime
        else:
            compute_datetime = datetime(year, month, day)

        # Plot the polar sky map or the xy path of the sun
        if plot_type == 'Polaire':
            file = File(plots.plot_polar_sky(eph, 'sun', compute_datetime), filename='polar_sky.png')
        else:
            file = File(plots.plot_xy_path(eph, 'sun', compute_datetime), filename='xy_path.png')

        embed = Embed(
            title='Éphémérides du soleil',
            description=f'Pour la date du {day}/{month}/{year} à {latitude}° de latitude et {longitude}° de longitude.',
            color=discord.Color.gold()
        )
        embed.set_image(url=f'attachment://{file.filename}')
        embed.add_field(name='Lever du soleil', value=sunrise.strftime('%H:%M:%S'), inline=False)
        embed.add_field(name='Coucher du soleil', value=sunset.strftime('%H:%M:%S'), inline=False)
        embed.add_field(name='Cartes du lieu d\'observation', value=f'[Google Maps]({google_maps_url}) - [Bing Maps]({bing_maps_url})', inline=False)

        await ctx.respond(embed=embed, file=file)

def setup(
    bot
):
    """
    Setup function to add the cog to the bot.

    Args:
        bot (commands.Bot): The bot instance.

    Returns:
        None
    """
    bot.add_cog(Sun(bot))
