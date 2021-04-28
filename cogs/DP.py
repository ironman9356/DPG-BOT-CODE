
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='your prefix')

class DP(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command(help="The Man, The Beard, the RAGE MONSTER himself", aliases=['ty'])
  async def tyler(self,ctx):
    embed=discord.Embed(title='<:ty_pog:823499904659750942>TYLER TONEY<:ty_pog:823499904659750942>',color=0x46e2ec,description="Tyler Toney is one of the Dude Perfect members. He is the youngest out of the group and has the most battle wins. His aliases are 'The Beard', 'TT', and 'TyNaTo'.")
    embed.add_field(name="Appearances",value="Ty hold most Battle wins, and is probably most known for him being, 'Rage Monster' in the Stereotypes series. Other appearances include Overtime in which he has played with Ninja, given a controversial top 10 movies list, and completed some Absurd Recurds.",inline=False)
    embed.add_field(name="Social Media",value="[Instagram](https://www.instagram.com/tylerntoney)\n[Twitter]( https://twitter.com/tylerntoney) ")
    embed.set_thumbnail(url="https://images2.vudu.com/person/1247992-300")
    await ctx.send(embed=embed)
  @commands.command(help="Do you follow the Dude Perfect YouTube Channel yet?!",aliases=['yt'])
  async def youtube(self,ctx):
    
    embed=discord.Embed(title="Dude Perfect YouTube Channels",color=0x46e2ec,description='Make sure to Subscribe to all three channels!\n\n[Dude Perfect](https://www.youtube.com/dudeperfect)\n[Dude Perfect Plus](https://www.youtube.com/dudeperfectplus)\n[Dude Perfect Gaming](https://www.youtube.com/dudeperfectgaming)')
    await ctx.send(embed=embed)
  @commands.command(help="Check out the Dudes on their Socials!", aliases=['socials'])
  async def social(self,ctx):
    embed=discord.Embed(title='Socials',description="Check out the Dude's socials",color=0x46e2ec)
    embed.add_field(name='INSTAGRAM',value='Check out them on Instagram\n[Dude Perfect](https://www.instagram.com/dudeperfect)\n[Dude Perfect Gaming](https://www.instagram.com/dudeperfectgaming)\n[Dude Perfect Editors](https://www.instagram.com/dpeditors/)\n[Coby](https://www.instagram.com/cobycotton)\n[Cody](https://www.instagram.com/cody_jones_)\n[Cory](https://www.instagram.com/corycotton)\n[Garrett](https://www.instagram.com/garretthilbert)\n[Tyler](https://www.instagram.com/tylerntoney)\n[Sparky](https://www.instagram.com/sparky_man4)')
    embed.add_field(name='TIKTOK',value='Check out them on TikTok\n[Dude Perfect](https://www.tiktok.com/@dudeperfect)')
    embed.add_field(name='TWITTER',value='Check out them on Twitter\n[Dude Perfect](https://www.twitter.com/dudeperfect)\n[Cory](https://twitter.com/CoryCotton)\n[Coby](https://twitter.com/CobyCotton)\n[Cody](https://twitter.com/Codes87)\n[Garrett](https://twitter.com/GarrettHilbert)\n[Tyler](https://twitter.com/TylerNToney)')
    await ctx.send(embed=embed)
  @commands.command(help="One day we will know the true Panda identity!")
  async def tiethepie(self,ctx):
    embed=discord.Embed(title="**Tie The Pie**",color=0x46e2ec,description='Subscribe to Dude Perfect to see the reveal of Panda\n**[Details](https://youtu.be/bFUZ5gruc0E)**ㅤㅤㅤㅤ**[Subscribe](http://bit.ly/SubDudePerfect)**')
    await ctx.send(embed=embed)
  @commands.command(help= 'Always in search of that elusive battle win')
  async def coby(self ,ctx):
    embed=discord.Embed(color=0x46e2ec,title='COBY COTTON',description='Coby Cotton is a shooter for Dude Perfect. He used to lose every battle until the Giant Sumo Battle. He has a twin brother name Cory Cotton.')
    embed.add_field(name='Appearances',value="Coby has only 2 battle wins, the least out of all the Dude Perfect Bros. He has been suspended from Cool Not Cool once for going over budget and buying a 100 dollar ostrich pillow. Coby went 29 episodes without winning his first battle when he won the Giant Sumo Battle against Garrett Hilbert",inline=False)
    embed.add_field(name="Social Media",value=" [Instagram](https://www.instagram.com/cobycotton)\n[Twitter](https://twitter.com/CobyCotton) ")
    embed.set_thumbnail(url="https://www.thefamouspeople.com/profiles/images/coby-cotton-1.jpg")
    await ctx.send(embed=embed)
  
  @commands.command(help="Tall Guy, Loud Guy, the Legend Himself")
  async def cody(self,ctx):
    embed=discord.Embed(title="CODY JONES",description="The tall man with the plan is Cody Jones. He is a fan of the show just don't let him enter the DP Gaming Room when the game is on the line.",color=0x46e2ec,inline=False)
    embed.add_field(name="Appearances",value="Cody has 9 battle wins and won the very first battle the Paper Airplane Battle in 2012. His most recent battle win was Metal Detector Battle 2. In Overtime 12 Cody bought the guys exotic cars including a Rolls Royce Lamborghini McLaren and a Bentley.",inline=False)
    embed.add_field(name="Social Media",value=" [Instagram](https://www.instagram.com/cody_jones_)\n[Twitter](https://twitter.com/codes87) ",inline=False)
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/T4QOw1Br53LKZoy3OIhkpX8zkHBdM8Lh3vXnvsv3Z_Y/https/www.gstatic.com/tv/thumb/persons/957509/957509_v9_ba.jpg?width=225&height=300")
    await ctx.send(embed=embed)
  @commands.command(help="Information about the DP Beans")
  async def dpbeans(self,ctx):
    embed=discord.Embed(title="<:dpbeans:836606529087733760>DUDE PERFECT BEANS!!<:dpbeans:836606529087733760>",description="Practice makes perfect. We lost track of how many different versions we made, but we call it Batch 5 as a nod to our 5 friends at DudePerfect. They helped us create the perfect bean…made with applewood smoked bacon, authentic Southwestern spice and real jalapeños for a robust not-too-hot flavor. Pound It Noggin!\n\n[DUDE PERFECT JALAPEÑO & BACON BEANS 12 PACK](https://seriousbeanco.com/products/dude-perfect-jalapeno-bacon-beans-12-pack) ",color=0x46e2ec)
    embed.set_thumbnail(url="https://i.ibb.co/JzRdVkr/Serious-Bean-Co-Jalapeno-Bacon-Article.png")
    await ctx.send(embed=embed)
  @commands.command(help="The Overtimve intro")
  async def intro(self,ctx):
    embed=discord.Embed(description=":musical_note:\nTall Guy, Beard, Twins, Purple Hoser\n\nDude Perfect's in Overtime\n\nTall Guy, Beard, Twins, Purple Hoser\n\nNow we're heading onto Overtime\n:musical_note:",color=0x5fb71b,title="OVERTIME")
    await ctx.send(embed=embed)
  @commands.command(help="Coby the rage monster!!")
  async def ragecoby(self,ctx):
    embed=discord.Embed(title=":rage: COBY RAGE!! :rage:")
    embed.set_image(url="https://media.giphy.com/media/kFlE6nqMX3Wu1d1CTh/giphy.gif?width=400&height=225")
    await ctx.send(embed=embed)
  @commands.command(help="Wanna watch all vids? You should check this out")
  async def playlist(self,ctx):
    embed=discord.Embed(title="YOUTUBE PLAYLIST",description="[Here is a playlist of all of Dude Perfects Vids!](https://www.youtube.com/watch?v=OFBsuEGhQkI&list=PLCsuqbR8ZoiDF6iBf3Zw6v1jYBNRfCuWC)",color=0x46e2ec)
    await ctx.send(embed=embed)
  @commands.command(help="Tie the sub count of Dude Perfect to pewdiepie find out the man behind the mask")
  async def panda(self,ctx):
    embed=discord.Embed(title="Panda",description="The Panda is a recurring figure on DP. It is currently unknown who they are, but DP says they will reveal him when they #TieThePie which means if they get as many subscribers as PewDiePie.",color=0x46e2ec)
    embed.add_field(name="Appearances",value="He appears in DP videos every once in a while, and was introduced to DP in a series of videos where the dudes tame him.",inline=False)
    embed.add_field(name="Social Media",value=" [Instagram](https://www.instagram.com/myfriendpanda/)\n[Twitter](https://twitter.com/Panda____Swag) ")
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/dudeperfect/images/b/b0/Panda.jpg/revision/latest/scale-to-width-down/250?cb=20150802232743")
    await ctx.send(embed=embed)

  

def setup(client):
  client.add_cog(DP(client))
