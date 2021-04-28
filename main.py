import discord
from discord.ext import commands 
import os
import re

intents = discord.Intents.all()

client = commands.Bot(
  command_prefix='your prefix',
  owner_ids = {your user id},
  case_insensitive=True ,
  intents=intents,
  strip_after_prefix=True,
  self_bot=False,
  activity=discord.Activity(type=discord.ActivityType.listening, name='-help')
  )

@client.event
async def on_ready():
  print(f'Logged in as {client.user}\nReady!')


#----Made by @Pi Boy#0175-----
@client.listen('on_message')
async def ned(message):  
    if message.author.bot:
        return
    elif ':ned'in message.content :
        return
    elif message.content == ' ned':
        await message.add_reaction (":ned:")
    elif message.content == 'ned':
        await message.add_reaction (":ned:")
    elif ' ned 'in message.content :
        await message.add_reaction(":ned:")


#"""MORE INFO ON HELP COMMAND HERE
# https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96#start"""
class MyHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
          destination = self.get_destination()
          for page in self.paginator.pages:
              emby = discord.Embed(description=page,color=discord.Color.random())
              await destination.send(embed=emby)
    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command),color=discord.Color.random())
        embed.add_field(name="Help", value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def on_help_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Error", description=str(error),color=discord.Color.random())
            await ctx.send(embed=embed)
        else:
            raise error
    async def send_error_message(self, error):
        embed = discord.Embed(title="Error", description=error,color=discord.Color.random())#COLOR HERE IF YOU WANT TO CHANGE
        channel = self.get_destination()
        await channel.send(embed=embed)

client.help_command = MyHelp()



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('token')