import discord
import os
import groq
from dotenv import load_dotenv
load_dotenv()
# Clave De Tokens del Bot
token = os.environ.get("TOKEN_BOT")
ai_key = os.environ.get("API_AI_GROQ")

#! AI
ai = groq.Groq(api_key = ai_key)

# Permits For The Bot
permits = discord.Intents.default()

bot = discord.Client(intents = permits)

@bot.event
async def on_ready():
    print("se Conecto el Bot")

bot.run(token)