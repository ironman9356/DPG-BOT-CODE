import discord
from discord.ext import commands


client = commands.Bot(command_prefix='your prefix',owner_ids = {your user id},case_insensitive=True ,intents=intents)

class Revive(commands.Cog):
  def __init__(self,client):
    self.client=client
  @commands.command(description='Usage:')
  async def revive(self,ctx):
    """Hurry! We gotta save the chat!!"""
    embed=discord.Embed(title='This chat is reviveable... very reviveable...',color=0x46e2ec)
    await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Revive(client))