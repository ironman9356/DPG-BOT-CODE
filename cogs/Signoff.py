import discord
from discord.ext import commands


client = commands.Bot(command_prefix='your prefix',owner_ids = {your user id},case_insensitive=True )

class Signoff(commands.Cog):
  def __init__(self,client):
    self.client=client
  @commands.command(description="Usage:")
  async def signoff(self,ctx):
    """Heading out? Hit us with the DP Sign-off! """
    embed=discord.Embed(description=f'**{ctx.author.mention} is signing off for now...**' ,color=0x46e2ec)
    embed.add_field(name='POUND IT! :punch:',value='\u200b',inline=False)
    embed.add_field(name='NOGGIN! :busts_in_silhouette:',value='\u200b',inline=False)
    embed.add_field(name='SEE YA!! :v:',value='\u200b',inline=False)
    embed.add_field(name=':billed_cap:     :arrow_right:     :movie_camera:',value='\u200b',inline=False)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('\U0001f44b')


def setup(client):
  client.add_cog(Signoff(client))