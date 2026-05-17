import discord
import os
from dotenv import load_dotenv
load_dotenv()
# Clave De Tokens del Bot
Tokens_Bot = os.environ.get("TOKEN_BOT")
# Permits For The Bot
permits = discord.Intents.default()

Bot = discord.Client(intents = permits)