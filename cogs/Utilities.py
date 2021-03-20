import discord
from discord.ext import commands
import asyncio


client = commands.Bot(command_prefix='your prefix',owner_ids = {your user id},case_insensitive=True)

class Utilities(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command(description="Usage:")
    async def ping(self,ctx):
      """Delay in sending messages"""
      await ctx.send(f'{round(self.client.latency * 1000)} ms')

    @commands.command(description="Usage:")
    async def avatar(self,ctx,member : discord.Member = None):
      """How does the profile picture of a person look? Find out!"""
      if not member:  # if Member is no mentioned
        member = ctx.message.author  # set Member as the author
      embed = discord.Embed(colour=discord.Colour.random())
      embed.set_image(url=member.avatar_url)
      await ctx.send(embed=embed)
    @avatar.error
    async def avatar_error(self,ctx, error): 
      await ctx.send('That user is not in this server')
    @commands.command(description="Usage:")
    async def bigemote(self,ctx,Custom_Emoji:discord.PartialEmoji):
      """BIG EMOTES"""
      embed = discord.Embed(colour=discord.Colour.random())
      embed.set_image(url=Custom_Emoji.url)
      await ctx.send(embed=embed)
      await asyncio.sleep(3)
      await ctx.message.delete()
    @bigemote.error
    async def bigemote_error(self,ctx, error): 
      msg=await ctx.send('**Usage** `-bigemote <custom emoji>`')
      await asyncio.sleep(3)
      await ctx.message.delete()
      await msg.delete()
      return



def setup(client):
    client.add_cog(Utilities(client))