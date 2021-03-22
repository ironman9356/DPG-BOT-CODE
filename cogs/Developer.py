import discord
from discord.ext import commands
import platform
import psutil
import time , datetime
import uptime
client = commands.Bot(command_prefix='your prefix',owner_ids = {your user id},case_insensitive=True )


class Developer(commands.Cog):
  def __init__(self,client):
    self.client=client
  @commands.command()
  @commands.is_owner()
  async def chstatus(self,ctx,act,*,nm):
    if act == "watch":
      await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=nm))
    if act == "listen":
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=nm))
                
    if act == "play":
        await self.client.change_presence(activity=discord.Game(name=nm))

        
    print("Status Changed")
  @chstatus.error
  async def chstatus_error(self,ctx, error): 
    await ctx.send('You are not the developer')
  

  @commands.command()
  @commands.is_owner()
  async def setstatus(self,ctx):
    await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='-help'))
    await ctx.send('Status reseted')
    print('Status reseted')
  @setstatus.error
  async def setstatus_error(self,ctx, error): 
    await ctx.send('You are not the developer')

def setup(client):
    client.add_cog(Developer(client))