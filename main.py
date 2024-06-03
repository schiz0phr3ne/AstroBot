import os

import discord
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Bot()

@bot.event
async def on_ready():
    """
    Load cogs and sync commands when the bot is ready.
    """
    cogs = ['moon', 'planets', 'sun']
    for cog in cogs:
        bot.load_extension(f'astrobot.cogs.{cog}')
        print(f'AstroBot - Loaded cog: {cog}')
    await bot.sync_commands()
    print(f'AstroBot - Logged in as {bot.user}')

bot.run(DISCORD_TOKEN)
