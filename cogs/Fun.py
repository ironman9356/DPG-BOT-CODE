import discord
from discord.ext import commands
import random
import asyncio
import re 
client = commands.Bot(command_prefix='your prefix')

def convert(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return f'{minutes} minutes {seconds} seconds'
class Fun(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command(help="Cant decide what to choose? Let DPG BOT decide!")
  async def choose(self,ctx, *choices: str):
    await ctx.send(f"I choose {random.choice(choices)} ", allowed_mentions=discord.AllowedMentions(everyone=False, roles=False))
  @commands.command(help="Take your chance at an awesome DP trickshot. Can you do it?!")
  async def trickshot(self,ctx):
    
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
  @commands.command(help=" Bottle Bust an un-expecting friend!",aliases=['bottlebust'])
  async def bb(self,ctx,member:discord.Member=None):
    if not member:
      member=ctx.author
    
    embed=discord.Embed(title=":rotating_light:             BOTTLE BUSTER ALERT            :rotating_light:",description=f"{ctx.author.mention} **BOTTLE BUSTED** {member.mention}")
    embed.set_image(url='https://i.ibb.co/x3899w9/Ty-BB.gif')
    await ctx.send(embed=embed)
    

  @commands.command(help=" Heads or tails, let the DPG BOT decide!",aliases=['coinflip'],name="cf")
  async def cf(self,ctx):
    
    x=random.randint(1,2)
    if x==1:
      embed=discord.Embed(title="You flipped a...",color=0x46e2ec)
      embed.set_image(url='https://i.ibb.co/Y3zVhL3/CFHeads.gif')
      msg= await ctx.reply(embed=embed,mention_author=False)
      await asyncio.sleep(5)
      embed.set_image(url='https://i.ibb.co/Y3zVhL3/CFHeads.gif')
      embed.set_footer(text="HEADS")
      await msg.edit(embed=embed,mention_author=False)
    elif x==2:
      embed=discord.Embed(title="You flipped a...",color=0x46e2ec)
      embed.set_image(url='https://i.ibb.co/bRpbPcd/CFTails.gif')
      msg= await ctx.reply(embed=embed,mention_author=False)
      await asyncio.sleep(5)
      embed.set_footer(text="TAILS")
      embed.set_image(url='https://i.ibb.co/bRpbPcd/CFTails.gif')
      await msg.edit(embed=embed,mention_author=False)



            
  @commands.command(help="Learn all there is to know about the dudes!")
  async def dpwiki(self,ctx):
    embed=discord.Embed(title='DP WIKI',description='[This](https://dudeperfect.fandom.com/wiki/Dude_Perfect_Wiki) is an awesome resource for all of the Dude Perfect stats and info!', color=0x46e2ec)
    await ctx.send(embed=embed)
  @commands.command(help="It's time for a dance party!")
  async def dance(self,ctx):
    
    embed=discord.Embed(title='PANDA DANCE PARTY!')
    embed.set_image(url='https://media.tenor.com/images/b0dcde6ad525effd15648871cf6810f6/tenor.gif')
    await ctx.send(embed=embed)
  @commands.command(help="Hurry! We gotta save the chat!!")
  async def revive(self,ctx):
    embed=discord.Embed(title='This chat is reviveable... very reviveable...',color=0x46e2ec)
    await ctx.send(embed=embed)
  @commands.command(help="RIP")
  async def rip(self,ctx):
    embed=discord.Embed(title='rip...')
    embed.set_image(url='https://images-ext-1.discordapp.net/external/MrJ-o7BNRToF65JmIHwov9oCPGWp6g701Nh17Y-ZO6w/%3Fitemid%3D19655727/https/media1.tenor.com/images/277661c97fedf4f2abee198f9cab7cea/tenor.gif')
    await ctx.send(embed=embed)
  @commands.command(help="Heading out? Hit us with the DP Sign-off! ")
  async def signoff(self,ctx):
    embed=discord.Embed(description=f'**{ctx.author.mention} is signing off for now...**' ,color=0x46e2ec)
    embed.add_field(name='POUND IT! :punch:',value='\u200b',inline=False)
    embed.add_field(name='NOGGIN! :busts_in_silhouette:',value='\u200b',inline=False)
    embed.add_field(name='SEE YA!! :v:',value='\u200b',inline=False)
    embed.add_field(name=':billed_cap:     :arrow_right:     :movie_camera:',value='\u200b',inline=False)
    embed.set_image(url="https://images-ext-2.discordapp.net/external/zmhbRjq6JYwh5xhNkNI6KXhh16oO96tJa8iKZ-J57HM/https/media.discordapp.net/attachments/821907733434597386/824039035424866344/giphy-downsized-medium.gif")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('\U0001f44b')

  @commands.command(help="Welcome a new memeber")
  async def welcome(self,ctx,member:discord.Member=None):
    if not member:
      embed=discord.Embed(title=f"WELCOME TO {ctx.guild.name}",description="Welcome **New Member**!",color=discord.Color.random())
    if member :
      embed=discord.Embed(title=f"WELCOME TO {ctx.guild.name}",description=f"Welcome **{member.name}**!",color=discord.Color.random())
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
  @welcome.error
  async def welcome_error(self,ctx, error): 
    embed=discord.Embed(title=f"WELCOME TO {ctx.guild.name}",description="Welcome **New Member**!",color=discord.Color.random())
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
  @commands.command(help="Call an emergency meeting  ")
  async def button(self, ctx,*, txt=None):
    if txt is None:
      txt="%20"
    name=txt.replace(" ","%20")    
    await ctx.send(f"https://vacefron.nl/api/emergencymeeting?text={name}")
  @commands.command(help="You can put yourself or put all others ")
  @commands.cooldown(1,300,commands.BucketType.user)
  async def vote(self,ctx,member:discord.Member=None):
    if not member:
      member=ctx.author
    bools=[True,False]
    colors=["black","blue","brown","cyan","darkgreen","lime","orange","pink","purple","red","white","yellow"]
    name=member.name.replace(" ","%20")
    await ctx.send(f"https://vacefron.nl/api/ejected?name={name}&impostor={random.choice(bools)}&crewmate={random.choice(colors)}")

  @vote.error
  async def vote_error( self ,ctx, error): 
    if isinstance(error, commands.CommandOnCooldown):
          await ctx.send(f":warning: You Cannot Vote for another: {convert(int(error.retry_after))}.")
    else:
      await ctx.send(error)
  @commands.command(help="Come join the DPG Minecraft Community Server!")
  @commands.is_owner()
  async def minecraftserver(self,ctx):
    embed=discord.Embed(title="DPG MINECRAFT SERVER",description="Below you can find information on ho to connect to the official: **DPG Minecraft Server**",color=0x46e2ec)
    embed.add_field(name="__Supported Consoles:__",value="- Java Version\n- Windows 10 Bedrock\n- Xbox\n- Nintendo Switch\n- Android or Iphone",inline=False)
    embed.add_field(name="__IP Address:__",value="IP Address: dpgaming.serveminecraft.net\n**NOTE: the address is 'serve' NOT 'server'**\nPort: 25565\n\nPlease watch the following instructional video for connecting to the DPG Minecraft Server: [HOW TO](https://www.youtube.com/watch?v=hnO1PFVvbmI)\nIf you ever need any help at all please go to the #minecraft channel in [DPG Nation server](https://discord.gg/A68YFtC). You may ping @Minecraft Mod at any time. This is a cross platform server between all devices that are currently available above. If you are on Bedrock Edition you will be marked with 'BR_' to indicate your a bedrock player playing on our Java Server.\n\nUnfortunately you will not be able to use custom skins if you are on Bedrock. We will keep you updated on any changes in the future.")
    await ctx.send(":mailbox: You've Got Mail!")
    await ctx.author.send(embed=embed)
def setup(client):
    client.add_cog(Fun(client))