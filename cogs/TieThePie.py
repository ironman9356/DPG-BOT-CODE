import discord
from discord.ext import commands


client = commands.Bot(command_prefix='your prefix',owner_ids = {your user id},case_insensitive=True )

class TieThePie(commands.Cog):
  def __init__(self,client):
    self.client=client
  @commands.command()
  async def tiethepie(self,ctx):
    embed=discord.Embed(title="**Tie The Pie**",color=0x46e2ec,description='Subscribe to Dude Perfect to see the reveal of Panda\n**[Details](https://youtu.be/bFUZ5gruc0E)**ㅤㅤㅤㅤ**[Subscribe](http://bit.ly/SubDudePerfect)**')
    await ctx.send(embed=embed)


  
def setup(client):
  client.add_cog(TieThePie(client))