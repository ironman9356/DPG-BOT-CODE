import discord
from discord.ext import commands
import asyncio
import time

client = commands.Bot(command_prefix="your prefix")

class Utilities(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command(description="Usage:")
    async def ping(self,ctx):
      """Delay in sending messages"""
      start = time.perf_counter()
      message = await ctx.send("Ping...")
      end = time.perf_counter()
      duration = (end - start) * 1000
      await message.edit(content='Pong! {:.2f}ms'.format(duration))

    @commands.command(description="Usage:")
    async def avatar(self,ctx,member : discord.Member = None):
      """How does the profile picture of a person look? Find out!"""
      if not member:  
        member = ctx.message.author 
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
      embed.set_footer(text=f"By {ctx.author}")
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

  @commands.command(help="Ask a question to your friends")
  
  async def poll(self,ctx,question,*options):
        if len(options) > 10:
            return await ctx.send("You cant have more than 10 options")
        final_options = ""
        for i in range(len(options)):
            if options[i] == "":
                continue
            final_options += f"{i + 1}. {options[i]}\n"

        embed = discord.Embed(title=question, description=final_options, color=0x46e2ec)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

        reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

        msg = await ctx.send(content=None, embed=embed)
        a = 0
        for v in range(len(options)):
            if options[v] == '':
                a += 1
                continue
            await msg.add_reaction(reactions[a])
            a += 1

            
  @commands.command(help="For suggesting stuff for your server")
  
  async def suggest(self,ctx,*,suggestion):
    embed=discord.Embed(title="Suggestion",description=suggestion,color=0x89aa00)
    embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
    suggest=await ctx.send(embed=embed)
    await suggest.add_reaction("👍")
    await suggest.add_reaction("👎")


def setup(client):
    client.add_cog(Utilities(client))