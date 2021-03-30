import discord
from discord.ext import commands
import random
import asyncio
client = commands.Bot(command_prefix='your prefix')

class Fun(commands.Cog):
  def __init__(self,client):
    self.client=client
  @commands.command(description="Usage:")
  async def choose(self,ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
  @commands.command(description="Usage:")
  async def trickshot(self,ctx):
    """Take your chance at an awesome DP trickshot. Can you do it?!"""
    rng=random.randint(0,5)
    if rng==5:
      with open("gtrickshot.txt") as questions:
        lines = []
        for line in questions:
            lines.append(line)
      embed=discord.Embed(title=f'{lines[random.randint(0,len(lines)-1)]}', color=0x5fb71b)
      await ctx.send(embed=embed)
    else:
      with open("btrickshot.txt") as questions:
        lines = []
        for line in questions:
            lines.append(line)
      embed=discord.Embed(title=f'{lines[random.randint(0,len(lines)-1)]}', color=0xe74c3c)
      await ctx.send(embed=embed)
# bad e74c3c
  @commands.command(description="Usage:",aliases=['bottlebust'])
  async def bb(self,ctx,member:discord.Member):
    """ Bottle Bust an un-expecting friend!"""
    embed=discord.Embed(title=":rotating_light:             BOTTLE BUSTER ALERT            :rotating_light:")
    embed.set_image(url='https://i.ibb.co/x3899w9/Ty-BB.gif')
    await ctx.send(embed=embed)
    await ctx.send(f'{ctx.author.mention} **BOTTLE BUSTED** {member.mention}')
  @bb.error
  async def whois_error(self,ctx, error): # This might need to be (error, ctx), I'm not sure
    await ctx.send('You need to mention a user\nSyntax: `-bb @user`') #who is gives user info  
  @commands.command(description="Usage:")
  async def cf(self,ctx):
    """ Heads or tails, let the DPG BOT decide!"""
    x=random.randint(1,2)
    if x==1:
      embed=discord.Embed(title="You flipped a...",color=0x46e2ec)
      embed.set_image(url='https://i.ibb.co/Y3zVhL3/CFHeads.gif')
      msg= await ctx.send(embed=embed)
      await asyncio.sleep(3)
      embed.set_image(url='https://i.ibb.co/Y3zVhL3/CFHeads.gif')
      embed.set_footer(text="HEADS")
      await msg.edit(embed=embed)
    elif x==2:
      embed=discord.Embed(title="You flipped a...",color=0x46e2ec)
      embed.set_image(url='https://i.ibb.co/bRpbPcd/CFTails.gif')
      msg= await ctx.send(embed=embed)
      await asyncio.sleep(3)
      embed.set_footer(text="TAILS")
      embed.set_image(url='https://i.ibb.co/bRpbPcd/CFTails.gif')
      await msg.edit(embed=embed)
  @commands.command(description="Usage:",aliases=['youtube'])
  async def yt(self,ctx):
    """Do you follow the Dude Perfect YouTube Channel yet?!"""
    embed=discord.Embed(title="Dude Perfect YouTube Channels",color=0x46e2ec,description='Make sure to Subscribe to all three channels!\n\n[Dude Perfect](https://www.youtube.com/dudeperfect)\n[Dude Perfect Plus](https://www.youtube.com/dudeperfectplus)\n[Dude Perfect Gaming](https://www.youtube.com/dudeperfectgaming)')
    await ctx.send(embed=embed)
  @commands.command(description="Usage:", aliases=['socials'])
  async def social(self,ctx):
    """Check out the Dudes on their Socials!"""
    embed=discord.Embed(title='Socials',description="Check out the Dude's socials",color=0x46e2ec)
    embed.add_field(name='INSTAGRAM',value='Check out them on Instagram\n[Dude Perfect](https://www.instagram.com/dudeperfect)\n[Dude Perfect Gaming](https://www.instagram.com/dudeperfectgaming)\n[Dude Perfect Editors](https://www.instagram.com/dpeditors/)\n[Coby](https://www.instagram.com/cobycotton)\n[Cody](https://www.instagram.com/cody_jones_)\n[Cory](https://www.instagram.com/corycotton)\n[Garrett](https://www.instagram.com/garretthilbert)\n[Tyler](https://www.instagram.com/tylerntoney)\n[Sparky](https://www.instagram.com/sparky_man4)')
    embed.add_field(name='TIKTOK',value='Check out them on TikTok\n[Dude Perfect](https://www.tiktok.com/@dudeperfect)')
    embed.add_field(name='TWITTER',value='Check out them on Twitter\n[Dude Perfect](https://www.twitter.com/dudeperfect)\n[Cory](https://twitter.com/CoryCotton)\n[Coby](https://twitter.com/CobyCotton)\n[Cody](https://twitter.com/Codes87)\n[Garrett](https://twitter.com/GarrettHilbert)\n[Tyler](https://twitter.com/TylerNToney)')
    await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))