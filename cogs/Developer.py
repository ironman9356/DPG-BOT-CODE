import discord
from discord.ext import commands
import platform
import psutil
import time , datetime
import uptime
client = commands.Bot(command_prefix='-',owner_ids = {548530397034577930,782904629523644446},case_insensitive=True)
start_time= time.time()


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
svmem = psutil.virtual_memory()
# print(f"Total: {get_size(svmem.total)}")
# print(f"Available: {get_size(svmem.available)}")
# print(f"Used: {get_size(svmem.used)}")
# print(f"Percentage: {svmem.percent}%")


class Developer(commands.Cog):
  def __init__(self,client):
    self.client=client
  @commands.command()
  @commands.is_owner()
  async def chstatus(self,ctx,act,nm):
    if act == "watch":
      await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=nm))
    if act == "listen":
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=nm))
                
    if act == "play":
        await self.client.change_presence(activity=discord.Game(name=nm))

        
    print("Status Changed")

  

  @commands.command()
  @commands.is_owner()
  async def setstatus(self,ctx):
    await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='-help'))
    await ctx.send('Status reseted')
    print('Status reseted')


def setup(client):
    client.add_cog(Developer(client))