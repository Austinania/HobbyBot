#python 3.10

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import botresponses

INTENTS = discord.Intents(messages = True, message_content = True, guilds = True, members = True, guild_typing = True, typing = True)
PREFIX1 = 'h!'
PREFIX = commands.when_mentioned_or(PREFIX1)

async def send_message(message, user_message, is_private):
    try:
        response = botresponses.bot_respond(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot = commands.Bot(intents=INTENTS, command_prefix=PREFIX)
    activity_string = 'on {} servers.'.format(len(bot.guilds)+1)
    
    @bot.event
    async def on_ready():
        print(f'{bot.user} is running.')
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_string + ' | ' + PREFIX1))
    
    @bot.command(
    name="ping",
    help="Help descriptor here",
    brief="Brief descriptor",
    )
    async def name_of_command_unless_name_is_seperately_declared(ctx):
        await ctx.send('Pong!')

    @bot.command(
    help="Generates a roster for JJBA-ASBR game",
    brief="Roster for JJBA-ASBR game",
    )
    async def JJTeam(ctx):
        jjteam = botresponses.bot_respond('jjbaasbr').split(',')
        await ctx.send(f'{jjteam[0]}')
        await ctx.send(f'{jjteam[1]}')
        await ctx.send(f'{jjteam[2]}')
        await ctx.send(f'{jjteam[3]}')
        await ctx.send(f'{jjteam[4]}')
        await ctx.send(f'{jjteam[5]}')
        await ctx.send(f'')


    bot.run(TOKEN)