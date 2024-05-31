import os
from datetime import datetime

import discord
from discord import Option
from dotenv import load_dotenv

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
    latitude: Option(float),
    longitude: Option(float),
    altitude: Option(int, default=0),
    date: Option(int, default=datetime.now().strftime('%d')),
    month: Option(int, default=datetime.now().strftime('%m')),
    year: Option(int, default=datetime.now().strftime('%Y'), )
):
    await ctx.respond([latitude, longitude, altitude, date, month, year])

bot.run(DISCORD_TOKEN)