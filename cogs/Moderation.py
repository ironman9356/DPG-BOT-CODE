import discord
from discord.ext import commands
import asyncio
import re
client = commands.Bot(command_prefix='-',owner_ids = {548530397034577930},case_insensitive=True)

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f'{hour} hours {minutes} minutes {seconds} seconds'
time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h":3600, "s":1, "m":60, "d":86400}
class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for v, k in matches:
            try:
                time += time_dict[k]*float(v)
            except KeyError:
                raise commands.BadArgument("{} is an invalid time-key! h/m/s/d are valid!".format(k))
            except ValueError:
                raise commands.BadArgument("{} is not a number!".format(v))
        return time


class Moderation(commands.Cog):
  def __init__(self,client):
    self.client=client




  #"""THIS WILL DM REGARDLESS OF KICK FAIL SO DONT KICK A NON KICKABLE PERSON"""  
  @commands.command(help="To kick people")
  @commands.has_permissions(kick_members=True)
  async def kick(self,ctx,member:discord.Member,*,reason=None):
    if member.id==ctx.author.id:
      msg=await ctx.send('You cant kick yourself ')
      await msg.add_reaction("🤦🏻‍♂️")
      return

    if not member:
      await ctx.send('You need to specify whom to kick ')
      return

    await member.send(f"You were kicked from `{ctx.guild.name}` for reason :{reason}")
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

  @kick.error
  async def kick_error( self ,ctx, error): 
    
    if isinstance(error, commands.MissingPermissions):
          await ctx.send("You dont have the perms to use this command")
    elif isinstance(error,commands.MissingRequiredArgument):
      await ctx.send('I cant kick no one lol')
    elif isinstance(error,commands.CommandInvokeError):
      await ctx.send('I cant kick that person')

    else:
      await ctx.send(error)

  #"""THIS WILL DM REGARDLESS OF BAN FAIL SO DONT BAN A NON BANABLE PERSON"""
  @commands.command(help="To ban people")
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    if member.id==ctx.author.id:
      msg=await ctx.send('You cant ban yourself ')
      await msg.add_reaction("🤦🏻‍♂️")
      return
    guild=ctx.guild
    await member.send(f"You were banned from `{ctx.guild.name}` for reason :{reason}")
    await guild.ban(member,reason=reason)
    await ctx.send(f'User {member.mention} has been banned')
  @ban.error
  async def ban_error( self ,ctx, error): 
    if isinstance(error, commands.MissingPermissions):
          await ctx.send("You dont have the perms to use this command")
    elif isinstance(error,commands.MissingRequiredArgument):
      await ctx.send('I cant ban no one lol')
    elif isinstance(error,commands.CommandInvokeError):
      await ctx.send('I cant ban that person')
    else:
      await ctx.send(error)
  @commands.command(help="Clear unwanted messages",aliases=['clean','purge'])
  @commands.has_permissions(manage_messages=True)
  async def clear(selx,ctx,amount=2):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)
    msg= await ctx.send('Done')
    await asyncio.sleep(2)
    await msg.delete()

  @commands.command(help="To unban people")
  @commands.has_permissions(administrator=True)
  async def unban(self,ctx,member:discord.User):
    if member.id==self.client.user.id :
      await ctx.send("I am not banned to unban myself")
      return
    if member.id==ctx.author.id:
      msg=await ctx.send('You cant kick yourself ')
      await msg.add_reaction("🤦🏻‍♂️")
      return
    member_id=member.id
    member = discord.Object(id=member_id)
    guild=ctx.guild
    await guild.unban(member)
    await ctx.send(f"Unbanned {member.mention}")
      
  @unban.error
  async def unban_error(self,ctx,error):
    if isinstance(error,commands.CommandInvokeError):
      await ctx.send("I cant unban that person")
    if isinstance(error,commands.MissingRequiredArgument):
      await ctx.send("Please specify whom to unban")
    else :
      await ctx.send(error)


 #"""MAY NOT WORK DEPENDING ON THE  @EVERYONE ROLE"""

  @commands.command(help="Mutes a member for the specified time- time in 2d 10h 3m 2s format ex:-mute @Someone 1d")
  @commands.has_permissions(manage_roles=True)
  async def mute(self, ctx, member:discord.Member,*,time:TimeConverter = None):
    permissions=discord.Permissions(send_messages=False,send_tts_messages=False)
    
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if mute_role is None:
      mute_role= await ctx.guild.create_role(name="Muted",color=0x818386,mentionable=False,hoist=False,permissions=permissions)
    
    await member.add_roles(mute_role)
    await member.send(f"You were muted in {ctx.guild.name} for {convert(int(time))} by {ctx.author}")
    await ctx.send(("Muted {} for {}s" if time else "Muted {}").format(member.mention, time))
    if time:
      await asyncio.sleep(time)
      await member.remove_roles(mute_role)
    else: 
      return
  @mute.error
  async def mute_error(self, ctx, error):
      if isinstance(error, commands.CheckFailure):
          pass
      if isinstance(error, commands.BadArgument):
          await ctx.send(error)
      if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Whom do I mute again ?")
      else:
        await ctx.send(error)
  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def unmute(self, ctx, member:discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    try:
      await member.remove_roles(role)
    except discord.HTTPException:
      await ctx.send(f"{member.mention} was not muted ")
      return
    await ctx.send(f"Unmuted {member.mention}")
  @unmute.error
  async def unmute_error(self,ctx,error):
    await ctx.send(error)
def setup(client):
    client.add_cog(Moderation(client))