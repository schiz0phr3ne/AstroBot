import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime

import discord
from discord import Embed, Option
from discord.ext import commands
from skyfield.api import Angle

from ephemeris import Ephemeris

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
        day: Option(int, default=int(datetime.now().strftime('%d')), description='Day of the month (default: today)'),
        month: Option(int, default=int(datetime.now().strftime('%m')), description='Month of the year (default: this month)'),
        year: Option(int, default=int(datetime.now().strftime('%Y')), description='Year (default: this year)')
    ):
        eph = Ephemeris(latitude, longitude, altitude, 'Europe/Paris')
        moonrise = eph.get_moonrise_time(datetime(year, month, day))
        moonset = eph.get_moonset_time(datetime(year, month, day))

        latitude_dms = Angle(degrees=latitude).dstr(format=u'{0}{1}°{2:02}′{3:02}.{4:0{5}}″')
        longitude_dms = Angle(degrees=longitude).dstr(format=u'{0}{1}°{2:02}′{3:02}.{4:0{5}}″')
        latitude_position = 'N' if latitude >= 0 else 'S'
        longitude_position = 'E' if longitude >= 0 else 'W'
        
        google_maps_url = f'https://www.google.com/maps/place/{latitude_dms}{latitude_position}+{longitude_dms}{longitude_position}'
        bing_maps_url = f'https://www.bing.com/maps?cp={latitude}~{longitude}&lvl=17'

        embed = Embed(
            title='Éphémérides de la lune',
            description=f'Pour la date du {day}/{month}/{year} à {latitude}° de latitude et {longitude}° de longitude.',
            color=discord.Color.og_blurple()
        )
        embed.add_field(name='Lever de la lune', value=moonrise.strftime('%H:%M:%S'), inline=False)
        embed.add_field(name='Coucher de la lune', value=moonset.strftime('%H:%M:%S'), inline=False)
        embed.add_field(name='Cartes', value=f'[Google Maps]({google_maps_url}) - [Bing Maps]({bing_maps_url})', inline=False)
        
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Moon(bot))
