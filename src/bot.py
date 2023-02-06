import logging
import os

import discord
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()

bot.load_extension("speech.speech_cog")

# Configuration of speech logger
logging.basicConfig(format="%(message)s")
logger = logging.getLogger("speech.speech_cog")
logger.setLevel(logging.WARNING)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


bot.run(os.getenv("TOKEN"))
