import os
from datetime import datetime

import discord
from discord import Option
from dotenv import load_dotenv

from astrobot.ephemeris import Ephemeris

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Bot()

@bot.event
async def on_ready():
    cogs = []
    for cog in cogs:
        bot.load_extension(f'astrobot.cogs.{cog}')
        print(f'Loaded cog {cog}')
    print(f'Logged in as {bot.user}')

@bot.command()
async def sun(
    ctx,
    latitude: Option(float, description='Latitude of the location'),
    longitude: Option(float, description='Longitude of the location'),
    altitude: Option(int, default=0, description='Altitude of the location'),
    day: Option(int, default=int(datetime.now().strftime('%d')), description='Day of the month (default: today)'),
    month: Option(int, default=int(datetime.now().strftime('%m')), description='Month of the year (default: this month)'),
    year: Option(int, default=int(datetime.now().strftime('%Y')), description='Year (default: this year)')
):
    eph = Ephemeris(latitude, longitude, altitude, 'Europe/Paris')
    sunrise = eph.get_sunrise_time(datetime(year, month, day))
    sunset = eph.get_sunset_time(datetime(year, month, day))
    await ctx.respond([latitude, longitude, altitude, day, month, year, sunrise, sunset])

bot.run(DISCORD_TOKEN)