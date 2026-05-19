import discord
import os
from dotenv import load_dotenv
load_dotenv()
# Clave De Tokens del Bot
token = os.environ.get("TOKEN_BOT")
# Permits For The Bot
permits = discord.Intents.default()

bot = discord.Client(intents = permits)

@bot.event
async def on_ready():
    print("se Conecto el Bot")

bot.run(token)