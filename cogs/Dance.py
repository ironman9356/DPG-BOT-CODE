# PANDA DANCE PARTY!
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='-',owner_ids = {548530397034577930},case_insensitive=True)

class Dance(commands.Cog):
  def __init__(self,client):
    self.client=client
  @commands.command(description="Usage:")
  async def dance(self,ctx):
    """ It's time for a dance party!"""
    embed=discord.Embed(title='PANDA DANCE PARTY!')
    embed.set_image(url='https://media.tenor.com/images/b0dcde6ad525effd15648871cf6810f6/tenor.gif')
    await ctx.send(embed=embed)




def setup(client):
  client.add_cog(Dance(client))