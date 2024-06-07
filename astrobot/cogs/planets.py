import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime

import discord
from discord import Embed, Option
from discord.ext import commands

import utils
from constants import PLANETS
from ephemeris import Ephemeris

class Planets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description='Get planet rise and set times for a given location and date')
    async def planet(
        self,
        ctx,
        planet: Option(str, description='Name of the planet', choices=PLANETS.keys()),
        latitude: Option(float, description='Latitude of the location'),
        longitude: Option(float, description='Longitude of the location'),
        altitude: Option(int, default=0, description='Altitude of the location'),
        day: Option(int, default=0, min_value=1, max_value=31, description='Day of the month (default: today)'),
        month: Option(int, default=0, min_value=1, max_value=12, description='Month of the year (default: this month)'),
        year: Option(int, default=0, min_value=1550, max_value=2650, description='Year (default: this year)')
    ):
        await ctx.defer()
        
        eph = Ephemeris(latitude, longitude, altitude, 'Europe/Paris')
        
        if day == 0:
            day = datetime.now().day
        if month == 0:
            month = datetime.now().month
        if year == 0:
            year = datetime.now().year
        
        planetrise = eph.get_planet_rise_time(datetime(year, month, day), PLANETS[planet])
        planetset = eph.get_planet_set_time(datetime(year, month, day), PLANETS[planet])

        google_maps_url = utils.get_google_maps_url(latitude, longitude)
        bing_maps_url = utils.get_bing_maps_url(latitude, longitude)

        embed = Embed(
            title=f'Éphémérides de la planète {planet}',
            description=f'Pour la date du {day}/{month}/{year} à {latitude}° de latitude et {longitude}° de longitude.',
            color=discord.Color.teal()
        )
        embed.add_field(name='Lever de la planète', value=planetrise.strftime('%H:%M:%S'), inline=False)
        embed.add_field(name='Coucher de la planète', value=planetset.strftime('%H:%M:%S'), inline=False)
        embed.add_field(name='Cartes du lieu d\'observation', value=f'[Google Maps]({google_maps_url}) - [Bing Maps]({bing_maps_url})', inline=False)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Planets(bot))