import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime

import discord
from discord import Embed, Option
from discord.ext import commands

from ephemeris import Ephemeris
import utils

class Moon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description='Get moonrise and moonset times for a given location and date')
    async def moon(
        self,
        ctx,
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
        
        moonrise = eph.get_moonrise_time(datetime(year, month, day))
        moonset = eph.get_moonset_time(datetime(year, month, day))

        google_maps_url = utils.get_google_maps_url(latitude, longitude)
        bing_maps_url = utils.get_bing_maps_url(latitude, longitude)

        embed = Embed(
            title='Éphémérides de la lune',
            description=f'Pour la date du {day}/{month}/{year} à {latitude}° de latitude et {longitude}° de longitude.',
            color=discord.Color.og_blurple()
        )
        embed.add_field(name='Lever de la lune', value=moonrise.strftime('%H:%M:%S'), inline=False)
        embed.add_field(name='Coucher de la lune', value=moonset.strftime('%H:%M:%S'), inline=False)
        embed.add_field(name='Cartes du lieu d\'observation', value=f'[Google Maps]({google_maps_url}) - [Bing Maps]({bing_maps_url})', inline=False)
        
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Moon(bot))
