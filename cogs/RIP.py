import discord
from discord.ext import commands


client = commands.Bot(command_prefix='your prefix',owner_ids = {your user id},case_insensitive=True )

class RIP(commands.Cog):
  def __init__(self,client):
    self.client=client
  @commands.command(description="Usage:")
  async def rip(self,ctx):
    """RIP"""
    embed=discord.Embed(title='rip...')
    embed.set_image(url='https://images-ext-1.discordapp.net/external/MrJ-o7BNRToF65JmIHwov9oCPGWp6g701Nh17Y-ZO6w/%3Fitemid%3D19655727/https/media1.tenor.com/images/277661c97fedf4f2abee198f9cab7cea/tenor.gif')
    await ctx.send(embed=embed)

def setup(client):
    client.add_cog(RIP(client))