import discord
from discord.ext import commands 
import os
import requests,json
from datetime import datetime 
import pytz 
apiid=os.getenv('appID')
complete_url='https://api.openweathermap.org/data/2.5/weather?q=Frisco&APPID='+apiid


client = commands.Bot(command_prefix='-',owner_ids = {548530397034577930,782904629523644446},case_insensitive=True )
greet={"00":"Night","01":"Night","02":"Night","03":"Night","04":"Night","05":"Morning","06":"Morning","07":"Morning","08":"Morning","09":"Morning","10":"Morning","11":"Morning","12":"Afternoon","13":"Afternoon","14":"Afternoon","15":"Afternoon","16":"Afternoon","17":"Evening","18":"Evening","19":"Evening","20":"Evening","21":"Night","22":"Night","23":"Night"}
col={"Night":0x1034a6,"Evening":0x7b68ee,"Afternoon":0xff8c00,"Morning":0x90ee90}
thumb={"Night":"https://images-ext-2.discordapp.net/external/3YAUA1DhOq5W3HUprLZ6dXKlWQhS9OL7Tn-fWHpzZq4/https/cdn4.iconfinder.com/data/icons/outdoors-3/460/night-512.png","Evening":"https://images-ext-2.discordapp.net/external/3YAUA1DhOq5W3HUprLZ6dXKlWQhS9OL7Tn-fWHpzZq4/https/cdn4.iconfinder.com/data/icons/outdoors-3/460/night-512.png","Afternoon":"https://images-ext-1.discordapp.net/external/nK4JDVDl2i2B8wKeLMHa69Nm2X7EwDLlr9ZHOzEak68/https/www.bnrconvention.com/wp-content/uploads/2017/04/coffee-icon-1.png","Morning":"https://images-ext-1.discordapp.net/external/nK4JDVDl2i2B8wKeLMHa69Nm2X7EwDLlr9ZHOzEak68/https/www.bnrconvention.com/wp-content/uploads/2017/04/coffee-icon-1.png"}
class Time(commands.Cog):
  def __init__(self,client):
    self.client=client
  @commands.command(description="Usage:")
  async def time(self,ctx):
    """The time in Frisco, Texas, where the Dude Perfect HQ is!"""
    response = requests.get(complete_url) 
    x = response.json()
    y = x["main"] 
    temp = y["temp"]
    z = x["weather"]
    temp=int(temp-273)
    far = (temp * 9/5) + 32
    IST = pytz.timezone('America/Chicago') 
    datetime_ist = datetime.now(IST)
    embed=discord.Embed(title=f'Good {greet[datetime_ist.strftime("%H")]}, {ctx.author} From Frisco, Texas!',description=f'**Time:** {datetime_ist.strftime("%I:%M:%S %p")}\n**Date:** {datetime_ist.strftime("%A, %B %d, %Y")}\n**Weather:** {z[0]["description"].title()} ({temp}°C , {far}°F)',color=col[greet[datetime_ist.strftime("%H")]])
    embed.set_thumbnail(url=thumb[greet[datetime_ist.strftime("%H")]])
    await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Time(client))