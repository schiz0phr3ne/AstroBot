"""
This module contains the `Planets` cog for AstroBot.

The `Planets` cog provides a command to get planet rise and set times for a given location and date.

Attributes:
    bot (commands.Bot): The bot instance.

Methods:
    planet: Get planet rise and set times for a given location and date.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime

import discord
from discord import Embed, File, Option
from discord.ext import commands

from ephemeris import Ephemeris
from constants import PLANETS, PLOT_TYPES
import plots
import utils

class Planets(commands.Cog):
    """
    Planets cog for AstroBot.

    This cog provides a command to get planet rise and set times for a given location and date.

    Attributes:
        bot (commands.Bot): The bot instance.

    Methods:
        planet: Get planet rise and set times for a given location and date.
    """
    def __init__(
        self,
        bot
    ):
        self.bot = bot

    @discord.slash_command(description='Get planet rise and set times for a given location and date')
    async def planet(
        self,
        ctx,
        planet: Option(str, description='Name of the planet', choices=PLANETS.keys()),
        latitude: Option(float, description='Latitude of the location'),
        longitude: Option(float, description='Longitude of the location'),
        altitude: Option(int, default=0, description='Altitude of the location'),
        plot_type: Option(str, choices=PLOT_TYPES.keys(), default='Polaire', description='Type of plot (default: polar sky)'),
        day: Option(int, default=0, min_value=1, max_value=31, description='Day of the month (default: today)'),
        month: Option(int, default=0, min_value=1, max_value=12, description='Month of the year (default: this month)'),
        year: Option(int, default=0, min_value=1550, max_value=2650, description='Year (default: this year)')
    ):
        """
        Get planet rise and set times for a given location and date.

        Args:
            planet (str): The name of the planet.
            latitude (float): The latitude of the location.
            longitude (float): The longitude of the location.
            altitude (int): The altitude of the location.
            day (int): The day of the month (default: today).
            month (int): The month of the year (default: this month).
            year (int): The year (default: this year).

        Usage:
            /planet planet latitude longitude altitude day month year

        Example:
            /planet mars 48.8566 2.3522 0 22 6 2024
        
        Returns:
            None
        """
        await ctx.defer()

        eph = Ephemeris(latitude, longitude, altitude, 'Europe/Paris')

        if day != 0 and month != 0 and year != 0:
            custom_date = True
        else:
            custom_date = False

        current_datetime = datetime.now()
        day = current_datetime.day if day == 0 else day
        month = current_datetime.month if month == 0 else month
        year = current_datetime.year if year == 0 else year

        planetrise = eph.get_planet_rise_time(datetime(year, month, day), PLANETS[planet])
        planetset = eph.get_planet_set_time(datetime(year, month, day), PLANETS[planet])

        google_maps_url = utils.get_google_maps_url(latitude, longitude)
        bing_maps_url = utils.get_bing_maps_url(latitude, longitude)

        # If the date is not the current date, compute the sky map for the custom date (at midnight)
        if not custom_date:
            compute_datetime = current_datetime
        else:
            compute_datetime = datetime(year, month, day)

        # Plot the polar sky map or the xy path of the planet
        if plot_type == 'Polaire':
            file = File(plots.plot_polar_sky(eph, PLANETS[planet], compute_datetime), filename='polar_sky.png')
        else:
            file = File(plots.plot_xy_path(eph, PLANETS[planet], compute_datetime), filename='xy_path.png')

        embed = Embed(
            title=f'Éphémérides de la planète {planet}',
            description=f'Pour la date du {day}/{month}/{year} à {latitude}° de latitude et {longitude}° de longitude.',
            color=discord.Color.teal()
        )
        embed.set_image(url=f'attachment://{file.filename}')
        embed.add_field(name='Lever de la planète', value=planetrise.strftime('%H:%M:%S'), inline=False)
        embed.add_field(name='Coucher de la planète', value=planetset.strftime('%H:%M:%S'), inline=False)
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
        None"""
    bot.add_cog(Planets(bot))
