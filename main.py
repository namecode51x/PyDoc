import discord
import os
import groq
from dotenv import load_dotenv
load_dotenv()
# Key Tokens Bot and AI
token = os.environ.get("TOKEN_BOT")
ai_key = os.environ.get("API_AI_GROQ")

#! AI
ai = groq.Groq(api_key = ai_key)
model_ai = "openai/gpt-oss-120b"

# Permits For The Bot
permits = discord.Intents.default()
permits.message_content = True

bot = discord.Client(intents = permits)

# It serves to notify the terminal that the bot has connected successfully.
@bot.event
async def on_ready():
    print("se Conecto el Bot")

@bot.event
async def on_message(message):
    """It's the heart of the project; it ensures the bot doesn't 
make mistakes with its messages and can receive 
and respond to user messages."""
    if message.author == bot.user:
        return
    message_list = [
    {"role": "user", "content": message.content}
]
    ai_message = await ai.chat.completions.create(model = model_ai, messages = message_list)
    respond = ai_message.choices [0].message.content
    await message.channel.send(respond)
bot.run(token)