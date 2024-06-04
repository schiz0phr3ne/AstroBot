import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from datetime import datetime, time
from zoneinfo import ZoneInfo

from discord import Embed
from discord.ext import commands, tasks
from dotenv import load_dotenv

from constants import NASA_API_APOD_URL, NASA_APOD_URL, NASA_LOGO_URL

load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

class NasaApod(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.send_nasa_apod.start()

    @tasks.loop(time=time(hour=13, minute=43, second=0, tzinfo=ZoneInfo('Europe/Paris')))
    async def send_nasa_apod(self):
        payload = {'api_key': NASA_API_KEY}
        channel = self.bot.get_channel(CHANNEL_ID)
        
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
            
            channel.send(embed=embed)
        except requests.exceptions.RequestException as e:
            channel.send(f'Erreur lors de la récupération de l\'APOD de la NASA: {e}')
    
    @send_nasa_apod.before_loop
    async def before_send_nasa_apod(self):
        await self.bot.wait_until_ready()
    
    send_nasa_apod.error
    async def on_send_nasa_apod_error(self, error):
        print(f'An error occurred in the send_nasa_apod task: {error}')

def setup(bot):
    bot.add_cog(NasaApod(bot))