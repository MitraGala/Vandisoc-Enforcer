from time import sleep
import os
from discord import Member
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!',intents=intents)
bot.remove_command('help')
@bot.event
async def on_ready():
    emoji = bot.get_guild(995971208938004560).emojis
    for i in emoji:
      if i.id == 1007912248108400720:
        global em
        em = i
      if i.id == 1000365650822311966:
        global ne
        ne = i
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='active')
async def active(ctx):
  await ctx.send("I'm up and running "+ctx.author.name)
@bot.command(name='verify')
async def verify(ctx,arg1: Member=None):
    server=ctx.guild
    channel = bot.get_channel(998442467533783082) # general
    channel2 =bot.get_channel(996179250635878470) # immi logs
    if (server.get_role(995971209294520370) in ctx.author.roles):
        if arg1 == None:
            await(await ctx.send("No user given")).delete(delay=1)
        else:
            giverole = server.get_role(995971209172885505) # serf
            await arg1.add_roles(giverole)
            giverole = server.get_role(995971209156100133) # citizen
            await arg1.add_roles(giverole)
            takerole = server.get_role(995971209156100135) # unverified
            await arg1.remove_roles(takerole)
            await channel.send("Welcome to the server "+arg1.mention+". Your entry was approved by "+ctx.author.name)
            await channel2.send(arg1.mention+"  as been verified by "+ctx.author.name+" ("+str(ctx.author.id)+").")
        await  ctx.message.delete()

@bot.command(name='deny')
async def deny(ctx,arg1: Member=None):
    server=ctx.guild
    channel = bot.get_channel(996179250635878470) # immi logs
    channel2 = bot.get_channel(998442467533783082) # general
    if server.get_role(995971209294520370) in ctx.author.roles:
        if arg1 == None:
            await(await ctx.send("No user given")).delete(delay=1)
        else:
            giverole = server.get_role(995971209156100134) # denied
            await arg1.add_roles(giverole)
            takerole = server.get_role(995971209156100135) # unverified
            await arg1.remove_roles(takerole)
            await channel.send(arg1.mention+" has been denied by "+ctx.author.name+" ("+str(ctx.author.id)+").")
            await channel2.send(arg1.mention+" has been denied by "+ctx.author.name+". Rip bozo.")
        await ctx.message.delete()

@bot.command(name='brazil')
async def brazil(ctx,arg1: Member=None):
    server=ctx.guild
    if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.author.id == 337730118489341952:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            giverole = server.get_role(995971209193869423) # brazil
            await arg1.add_roles(giverole)
            await ctx.send(arg1.mention+" has been sent to Brazil!")

@bot.command(name='unbrazil')
async def unbrazil(ctx,arg1: Member=None):
    server=ctx.guild
    if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.author.id == 337730118489341952:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            takerole = server.get_role(995971209193869423) # brazil
            await arg1.remove_roles(takerole)
            await ctx.send(arg1.mention+" has been let out of brazil.")

@bot.command(name='changspeak')
async def changspeak(ctx,arg1: Member=None):
    server=ctx.guild
    if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.author.id == 337730118489341952:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            giverole = server.get_role(995971209193869422)
            if giverole in arg1.roles:
                await arg1.remove_roles(giverole)
                await ctx.send(arg1.mention+" has been undeported.")
            else:
                await arg1.add_roles(giverole)
                await ctx.send(arg1.mention+" has been deported!")
              
@bot.command(name='stfu')
async def stfu(ctx,arg1: Member=None):
    server=ctx.guild
    if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.author.id == 337730118489341952:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            giverole = server.get_role(995971209185464359)
            if giverole in arg1.roles:
                await arg1.remove_roles(giverole)
                await ctx.send(arg1.mention+" is allowed to speak normally again.")
            else:
                await arg1.add_roles(giverole)
                await ctx.send(arg1.mention+" has been told to stfu!")

@bot.command(name='sexy')
async def sexy(ctx,arg1: Member=None):
    server=ctx.guild
    if ctx.author.id == 337730118489341952:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            giverole = server.get_role(995971209009315871) # sexy
            await arg1.add_roles(giverole)
            await ctx.send(arg1.mention+" has been declared to be sexy!")

@bot.command(name='serb')
async def serb(ctx,arg1: Member=None):
    server=ctx.guild
    if ctx.author.id == 878946730840846356:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            giverole = server.get_role(995971209260970061) # sexy
            await arg1.add_roles(giverole)
            await ctx.send(arg1.mention+" has been declared Serb worthy!")

@bot.command(name='amber')
async def amber(ctx):
  await ctx.send('This command, it does absolutely nothing other than give this response. Try it, it\'s real')


@bot.command(name='daga')
async def sexy(ctx,arg1: Member=None):
    server=ctx.guild
    if ctx.author.id == 812048903599292466:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            giverole = server.get_role(995971209248383005) # daga squad
            await arg1.add_roles(giverole)
            await ctx.send(arg1.mention+" has been declared to be part of the Ratdaga Skwad <3")

@bot.command(name='toes')
async def toes(ctx,arg1: Member=None):
    server=ctx.guild
    if ctx.author.id == 668324327585873920:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            giverole = server.get_role(999826776857518162) # daga squad
            await arg1.add_roles(giverole)
            await ctx.send(arg1.mention+" is now world renowned for sucking toes.")

@bot.command(name='serf')
async def serf(ctx):
  if ctx.author.id == 337730118489341952:
    server=ctx.guild
    serf = server.get_role(995971209172885505)
    await ctx.message.delete()
    await ctx.send(serf.mention, delete_after = 0.5)

@bot.command(name="moderation")
async def moderation(ctx):
  server=ctx.guild
  if (server.get_role(995971209294520370) in ctx.author.roles):
    await ctx.send("https://media.discordapp.net/attachments/998442467533783082/999265268733841478/387d01d456cc9d6f2ada7d4f81245b41.png")

@bot.command(name="checkxp")
async def checkxp(ctx, num = None):
  if num != None:
    try:
      num = int(num)
      if num>0:
        xp = 10*(num-1)*(3*num+10)
        await ctx.send(str(xp))
      else:
        await ctx.sent('Please give a non-zero positive number.')
    except:
      await ctx.send("Please give a level number (positive whole number) for me to check the xp needed.")

@bot.command(name='checklevel')
async def checklevel(ctx, num = None):
  if num != None:
    try:
      num = int(num)
      if num>0:
        level = (-7+((6*num+845)/5)**0.5)/6
        level_int = int(level - (level%1))
        rem = int((level%1)*100)
        await ctx.send("Level " + str(level_int) + " and " + str(rem) + "% to the next level")
      else:
        await ctx.sent('Please give a non-zero positive number.')
    except:
      await ctx.send("Please give the amount of xp to convert to levels.")

bot.run(TOKEN)
