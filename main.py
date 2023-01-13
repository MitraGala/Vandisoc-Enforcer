from time import sleep
import os, filecmp, urllib.request, pickle, random
from discord import Member
from discord import Intents
from discord.ext import commands

TOKEN = open("key.txt", "r").read()
intents = Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)
bot.remove_command('help')
@bot.event
async def on_ready():
    emoji = bot.get_guild(995971208938004560).emojis
    for i in emoji:
      if i.id == 1007912248108400720:
        global em
        em = i
      if i.id == 996168288168050809:
        global tr
        tr = i
    print(f'{bot.user.name} has connected to Discord!')
    
@bot.event
async def on_message(ctx):
  if "1984" in ctx.content:
    await ctx.add_reaction(em)
  '''if ctx.author.id == 583377694364794917:
    await ctx.add_reaction("\N{NERD FACE}")
    await ctx.add_reaction("\N{PILE OF POO}")
    await ctx.add_reaction(tr)'''
  await bot.process_commands(ctx)

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

@bot.command(name='mitra')
async def verify(ctx):
    server=ctx.guild
    channel = bot.get_channel(998442467533783082) # general
    channel2 =bot.get_channel(996179250635878470) # immi logs
    if ctx.author.id == 337730118489341952:
        takerole = server.get_role(995971209156100135) # unverified
        await ctx.author.remove_roles(takerole)
        await channel.send(ctx.author.mention+" bot-abused his way into the server.")
    await ctx.message.delete()

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

@bot.command(name='bam')
async def bam(ctx,arg1: Member=None,*arg2):
    server=ctx.guild
    if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.author.id == 337730118489341952:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            if len(arg2) == 0:
                a = ""
                b = ""
            else:
                a = " for "
                b = " ".join(arg2)
            await ctx.send(arg1.mention+" has been bammed"+a+b+"!")


@bot.command(name='malaysia', aliases=['Malaysia', 'malay', 'Malay'])
async def brazil(ctx,arg1: Member=None):
    server=ctx.guild
    if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.author.id == 337730118489341952:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            giverole = server.get_role(995971209193869423) # brazil
            await arg1.add_roles(giverole)
            await ctx.send(arg1.mention+" has been sent to Malaysia!")

@bot.command(name='unmalaysia', aliases=['Unmalaysia', 'unmalay', 'Unmalay'])
async def unbrazil(ctx,arg1: Member=None):
    server=ctx.guild
    if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.author.id == 337730118489341952:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            takerole = server.get_role(995971209193869423) # brazil
            await arg1.remove_roles(takerole)
            await ctx.send(arg1.mention+" has been let out of Malaysia.")

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
    if ctx.author.id in [337730118489341952,831268691722108990]:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            giverole = server.get_role(995971209009315871) # sexy
            await arg1.add_roles(giverole)
            await ctx.send(arg1.mention+" has been declared to be sexy!")

@bot.command(name='awesomecaracal')
async def caracal(ctx,arg1: Member=None):
    server=ctx.guild
    if ctx.author.id == 302876467434618881:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            giverole = server.get_role(1016908009559052338) # sexy
            await arg1.add_roles(giverole)
            await ctx.send("awesomecaracal")

@bot.command(name='reddy')
async def reddy(ctx,arg1: Member=None):
    server=ctx.guild
    if ctx.author.id == 741873798537543721:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            giverole = server.get_role(1024866900783665293) # sexy
            await arg1.add_roles(giverole)
            await ctx.send(arg1.mention+" is now part of the Reddy caste!")
            
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

@bot.command(name = 'unserb', aliases=['kosovar', 'kosovo'])
async def unserb(ctx,arg1: Member=None):
    server=ctx.guild
    if ctx.author.id == 878946730840846356:
        if arg1 == None:
            await ctx.send("No user given")
        else:
            takerole = server.get_role(995971209260970061) # sexy
            await arg1.remove_roles(takerole)
            await ctx.send(arg1.mention+" has been caught recognising Kosovo!")

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

@bot.command(name="nerdtime")
async def nerdtime(ctx):
    server=ctx.guild
    if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.author.id == 337730118489341952:
        r = server.get_role(995971209277755411)
        tex = server.get_member(1017780774143008838)
        if r in tex.roles:
            await tex.remove_roles(r)
            await ctx.send("Nerdin' time is over")
        else:
            await tex.add_roles(r)
            await ctx.send("It's nerdin' time")

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
        await ctx.send('Please give a non-zero positive number.')
    except:
      await ctx.send("Please give the amount of xp to convert to levels.")

@bot.command(name='update')
async def update(ctx):
    server=ctx.guild
    if ctx.author.id == 835099961128910848 or ctx.author.id == 337730118489341952:
        url = 'https://raw.githubusercontent.com/MitraGala/Vandisoc-Enforcer/master/main.py'
        urllib.request.urlcleanup()
        urllib.request.urlretrieve(url, 'tempcode')
        sameFile = filecmp.cmp('main.py', 'tempcode')
        if not sameFile:
            await ctx.send("Updating...")
            quit()
        else:
            await ctx.send("Vandisoc is fully updated.")

@bot.command(name='set')
async def set(ctx, arg1):
    server=ctx.guild
    if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.message.channel.id == 996034231539085412:
        pastapath = "pastas/"+arg1
        pasta = {}
        pasta['userid']=ctx.author.id
        startlen = 6+len(arg1)
        pasta['content']=ctx.message.content[startlen:]
        if os.path.exists(pastapath):
            oldpasta = pickle.load(open(pastapath, "rb"))
            if oldpasta['userid'] == pasta['userid']:
                await ctx.send("Set pasta **" + arg1 + "**.")
                pickle.dump(pasta, open(pastapath, "wb"))
            else:
                await ctx.send("Pasta is already owned by user #"+str(oldpasta['userid']))
        else:
            await ctx.send("Set pasta **" + arg1 + "**.")
            pickle.dump(pasta, open(pastapath, "wb"))

@bot.command(name='pasta')
async def pasta(ctx, arg1):
    server=ctx.guild
    if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.message.channel.id == 996034231539085412:
        pastapath = "pastas/"+arg1
        if os.path.exists(pastapath):
            pasta = pickle.load(open(pastapath, "rb"))
            await ctx.send(pasta['content'].replace("@", "#"))
        else:
            await ctx.send("Pasta does not exist.")
    
@bot.command(name='roll')
async def roll(ctx, arg1):
    server=ctx.guild
    await ctx.send("You rolled " + str(random.randint(1,int(arg1))))
    
@bot.command(name='rps')
async def rps(ctx, userChoice):
    botChoice = random.randint(0,2)
    results = [['We tied!','You lost!','You won!'],['You won!','We tied!','You lost!'],['You lost!','You won!','We tied!']]
    userOptions = {'rock':0,'r':0,'paper':1,'p':1,'scissors':2,'s':2}[userChoice]
    await ctx.send('I chose ' + ['rock','paper','scissors'][botChoice] + '. ' + results[userOptions][botChoice])
    
@bot.command(name='wubblu')
async def wubblu(ctx):
    await ctx.send(pickle.load(open('wubblu.songs', "rb"))[random.randint(0,44)])

@bot.command(name='flip')
async def flip(ctx):
    results = ['Heads', 'Tails']
    await ctx.send(results[random.randint(0,1)])

@bot.command(name='news')
async def news(ctx, newslink):
    channel = bot.get_channel(1060796345826422854)
    server=ctx.guild
    if (server.get_role(1063344840651313192) in ctx.author.roles) or (server.get_role(995971209294520370) in ctx.author.roles):
        if newslink[:4] == 'http':
            await channel.send(newslink)    
            await ctx.message.delete()
        else:
            await ctx.send('Invalid link')
    
@bot.command(name='breaking')
async def breaking(ctx, newslink):
    channel = bot.get_channel(1060796345826422854)
    server=ctx.guild
    if (server.get_role(1063344840651313192) in ctx.author.roles) or (server.get_role(995971209294520370) in ctx.author.roles):
        if newslink[:4] == 'http':
            await channel.send('<@&1063333711187300433> ' + newslink)    
            await ctx.message.delete()
        else:
            await ctx.send('JESSE..,,,,.')
    
bot.run(TOKEN)
