#python 3.10

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import botresponses

INTENTS = discord.Intents(messages = True, message_content = True, guilds = True, members = True, guild_typing = True, typing = True)
PREFIX = 'h!'  # commands.when_mentioned_or('h!')

async def send_message(message, user_message, is_private):
    try:
        response = botresponses.bot_respond(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    client = discord.Client(intents=INTENTS)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is running.')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
    
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        # if contains global PREFIX, interprets message, otherwise ignores
        if user_message[0:len(PREFIX)] == PREFIX:
            is_prefixed = True
            user_message = user_message[len(PREFIX):]
            await send_message(message, user_message, is_prefixed=is_prefixed)
            print(f'Command initiated by {username} ({channel})')
        else:
            pass
            
    client.run(TOKEN)