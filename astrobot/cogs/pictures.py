"""
This module contains the cogs for sending the Astrobin Image of the Day and the NASA Astronomy Picture of the Day.

AstrobinIotd:
    - Sends the Astrobin Image of the Day to a specific channel.
    - Automatically triggered at 9:00 AM every day.

NasaApod:
    - Sends the NASA Astronomy Picture of the Day to a specific channel.
    - Automatically triggered at 9:00 AM every day.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from datetime import datetime, time
from zoneinfo import ZoneInfo

from discord import Embed
from discord.ext import commands, tasks
from dotenv import load_dotenv

from constants import (
    ASTROBIN_API_IOTD_URL,
    ASTROBIN_BASE_URL,
    ASTROBIN_LOGO_URL,
    ASTROBIN_API_URL,
    ASTROBIN_USERS_URL,
    NASA_API_APOD_URL,
    NASA_APOD_URL,
    NASA_LOGO_URL,
)

load_dotenv()
ASTROBIN_API_KEY = os.getenv("ASTROBIN_API_KEY")
ASTROBIN_API_SECRET = os.getenv("ASTROBIN_API_SECRET")
ASTROBIN_CHANNEL = int(os.getenv("ASTROBIN_CHANNEL"))
NASA_API_KEY = os.getenv("NASA_API_KEY")
NASA_CHANNEL = int(os.getenv("NASA_CHANNEL"))

class AstrobinIotd(commands.Cog):
    """
    Astrobin IOTD cog for AstroBot.
    
    This cog provides a task to send the Astrobin Image of the Day to a specific channel.
    
    Attributes:
        bot (commands.Bot): The bot instance.
    
    Methods:
        send_astrobin_iotd: Send the Astrobin Image of the Day to a specific channel.
    """
    def __init__(
        self,
        bot
    ):
        self.bot = bot
        self.send_astrobin_iotd.start()

    @tasks.loop(time=time(hour=9, minute=0, second=0, tzinfo=ZoneInfo('Europe/Paris')))
    async def send_astrobin_iotd(
        self
    ):
        """
        Send the Astrobin Image of the Day to a specific channel.
        
        Args:
            None
        
        Usage:
            Automatically triggered at 9:00 AM every day.
        
        Returns:
            None
        """
        channel = self.bot.get_channel(ASTROBIN_CHANNEL)
        astrobin_api_url = f'{ASTROBIN_BASE_URL}/{ASTROBIN_API_URL}{ASTROBIN_API_IOTD_URL}'
        payload = {
            'api_key': ASTROBIN_API_KEY,
            'api_secret': ASTROBIN_API_SECRET,
            'format': 'json',
        }

        try:
            response = requests.get(astrobin_api_url, params=payload, timeout=10)
            response.raise_for_status()
            data = response.json()
            astrobin_iotd_url = f'{ASTROBIN_BASE_URL}/{data["objects"][0]["image"]}'

            try:
                response = requests.get(astrobin_iotd_url, params=payload, timeout=10)
                response.raise_for_status()
                data = response.json()

                title = data['title']
                description = data['description']
                image_url = f'{ASTROBIN_BASE_URL}/{data["hash"]}'
                embed_image_url = data['url_hd']
                author = data['user']
                author_url = f'{ASTROBIN_USERS_URL}{author}'

                if len(description) > 1024:
                    description = description[:1021] + '...'

                embed = Embed(
                    title=f'Astrobin IOTD du {datetime.now().strftime("%d/%m/%Y")}',
                    url=image_url
                )
                embed.add_field(name=title, value=description, inline=False)
                embed.add_field(name=f'Par {author}', value=author_url, inline=False)
                embed.set_thumbnail(url=ASTROBIN_LOGO_URL)
                embed.set_image(url=embed_image_url)

                await channel.send(embed=embed)
            except requests.exceptions.RequestException as e:
                await channel.send(f'Erreur lors de la récupération de l\'IOTD d\'Astrobin (étape 2) : {e}')
        except requests.exceptions.RequestException as e:
            await channel.send(f'Erreur lors de la récupération de l\'IOTD d\'Astrobin (étape 1) : {e}')

    @send_astrobin_iotd.before_loop
    async def before_send_astrobin_iotd(
        self
    ):
        """
        Wait for the bot to be ready before starting the task.
        
        Args:
            None
        
        Returns:
            None
        """
        await self.bot.wait_until_ready()

    @send_astrobin_iotd.error
    async def on_send_astrobin_iotd_error(
        self, 
        error
    ):
        """
        Log any errors that occur during the task.
        
        Args:
            error (Exception): The error that occurred.
        
        Returns:
            None
        """
        print(f'An error occurred in the send_astrobin_iotd task: {error}')

class NasaApod(commands.Cog):
    """
    NASA APOD cog for AstroBot.
    
    This cog provides a task to send the NASA Astronomy Picture of the Day to a specific channel.
    
    Attributes:
        bot (commands.Bot): The bot instance.
    
    Methods:
        send_nasa_apod: Send the NASA Astronomy Picture of the Day to a specific channel.
    """
    def __init__(
        self,
        bot
    ):
        self.bot = bot
        self.send_nasa_apod.start()

    @tasks.loop(time=time(hour=9, minute=0, second=0, tzinfo=ZoneInfo('Europe/Paris')))
    async def send_nasa_apod(
        self
    ):
        """
        Send the NASA Astronomy Picture of the Day to a specific channel.
        
        Args:
            None
        
        Usage:
            Automatically triggered at 9:00 AM every day.
        
        Returns:
            None
        """
        payload = {'api_key': NASA_API_KEY}
        channel = self.bot.get_channel(NASA_CHANNEL)

        try:
            response = requests.get(NASA_API_APOD_URL, params=payload, timeout=10)
            response.raise_for_status()
            data = response.json()

            title = data['title']
            explanation = data['explanation']
            media_type = data['media_type']
            media_url = data['url']

            if len(explanation) > 1024:
                explanation = explanation[:1021] + '...'

            embed = Embed(
                title=f'NASA APOD du {datetime.now().strftime("%d/%m/%Y")}',
                url=NASA_APOD_URL
            )
            embed.add_field(name=title, value=explanation, inline=False)
            embed.set_thumbnail(url=NASA_LOGO_URL)

            if media_type == 'image':
                embed.set_image(url=media_url)
            else:
                embed.add_field(name='Lien vers la vidéo :', value=media_url, inline=False)

            await channel.send(embed=embed)
        except requests.exceptions.RequestException as e:
            await channel.send(f'Erreur lors de la récupération de l\'APOD de la NASA : {e}')

    @send_nasa_apod.before_loop
    async def before_send_nasa_apod(
        self
    ):
        """
        Wait for the bot to be ready before starting the task.
        
        Args:
            None
        
        Returns:
            None
        """
        await self.bot.wait_until_ready()

    send_nasa_apod.error
    async def on_send_nasa_apod_error(self, error):
        """
        Log any errors that occur during the task.
        
        Args:
            error (Exception): The error that occurred.
        
        Returns:
            None
        """
        print(f'An error occurred in the send_nasa_apod task: {error}')

def setup(
    bot
):
    """
    Setup function for the Astrobin IOTD and NASA APOD cogs.
    
    Args:
        bot (commands.Bot): The bot instance.
    
    Returns:
        None
    """
    bot.add_cog(AstrobinIotd(bot))
    bot.add_cog(NasaApod(bot))
