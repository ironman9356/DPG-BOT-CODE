import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='your prefix')

class Monsties(commands.Cog):
  def __init__(self,client):
    self.client=client
  @commands.command(description="Usage:")
  async def monstie(self,ctx):
    """Check your monstie crack with the official 'Monstie-Meter'"""
    embed=discord.Embed(title="**MONSTIE METER**", description=f"{ctx.author.mention}'s Monstie crack scored a {random.randint(0,6)} on the Monstie Meter!", color=0xf0f0f0)
    embed.set_thumbnail(url='https://www.uokpl.rs/fpng/f/113-1132338_monster-energy-white.png')
    await ctx.send(embed=embed)
  @commands.command(description="Usage:",aliases=['vipmonstie'])
  async def mvpmonstie(self,ctx):
    """Check your monstie crack with the official 'MVP Monstie-Meter'"""
    embed=discord.Embed(title="**MVP MONSTIE METER**", description=f"{ctx.author.mention}'s Monstie crack scored a {random.randint(7,11)} on the Monstie Meter!", color=0xe4d00a)
    embed.set_thumbnail(url='https://i.ibb.co/McRhw2y/Monstie-Gold.png')
    await ctx.send(embed=embed)
  @commands.command(description="Usage:")
  async def adminmonstie(self,ctx):
    """Check your monstie crack with the official 'Admin Monstie-Meter'"""
    embed=discord.Embed(title="**ADMIN MONSTIE METER**", description=f"{ctx.author.mention}'s Monstie crack scored a {random.randint(12,25)} on the Monstie Meter!", color=0x6699cc)
    embed.set_thumbnail(url='https://www.monsterenergy.com/media/uploads_image/2020/01/22/auto/800/2811c4db068e6afbeaf6f0fcf36769b1.png?mod=v1_90fd6dec396a042bd0cdd25ddbce6f14')
    await ctx.send(embed=embed)
  @commands.command(description="Usage:")
  async def chatmonstie(self,ctx):
    """To wake the chat up when its sleepy"""
    with open("questions.txt") as questions:
      lines = []
      for line in questions:
         lines.append(line)
    embed=discord.Embed(title=f'{lines[random.randint(0,len(lines)-1)]}', color=0x46e2ec)#, description="\u200b"
    embed.add_field(name='This chat is a little sleepy.',value='Answer the question to give the chat a little pep. How energizing...just like Sparky drinking a monstie.')
    embed.set_image(url='https://i.ibb.co/xYMQ3vN/discussgif.gif')
    await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Monsties(client))