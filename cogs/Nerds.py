import discord
from discord.ext import commands
import platform
import psutil
import time , datetime
import uptime
client = commands.Bot(command_prefix='-',owner_ids = {548530397034577930,782904629523644446},case_insensitive=True)


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


class Nerds(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command(aliases=['stats'])
  async def status(self,ctx):
    """For the nerds"""
    embed=discord.Embed(title='DPG BOT Status',color=discord.Colour.random())
    embed.set_author(name=self.client.user,icon_url=self.client.user.avatar_url)
    embed.add_field(name='Servers',value=len(self.client.guilds))
    embed.add_field(name='Python Version',value=platform.python_version())
    up=uptime.uptime()
    day = up // (24 * 3600)
    up = up % (24 * 3600)
    hour = up // 3600
    up %= 3600
    mins = up // 60
    up %= 60
    sec = up
    tosend=f'{int(day)} days {int(hour)} hours {int(mins)} mins {int(sec)} secs'

    embed.add_field(name='Uptime',value=tosend)
    embed.add_field(name='Process Memory',value=f"Total: {get_size(svmem.total)}\nAvailable: {get_size(svmem.available)}\nUsed: {get_size(svmem.used)}\nPercentage: {svmem.percent}%")
    await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Nerds(client))