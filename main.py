import discord
from discord.ext import commands 
import os
import re

intents = discord.Intents.all()
import keep_alive

keep_alive.keep_alive()
client = commands.Bot(command_prefix='-',owner_ids = {548530397034577930,782904629523644446},case_insensitive=True ,intents=intents)
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='-help'))
  print(f'Logged in as {client.user}\nReady!')


@client.listen('on_message')
async def ned(message):  
    if message.author.bot:
        return
    elif ':ned'in message.content :
        return
    elif message.content == ' ned':
        await message.add_reaction ("<a:ned:821427067068481616>")
    elif message.content == 'ned':
        await message.add_reaction ("<a:ned:821427067068481616>")
    elif ' ned'in message.content :
        await message.add_reaction("<a:ned:821427067068481616>")




for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
token=os.getenv('TOKEN')
client.run(token)