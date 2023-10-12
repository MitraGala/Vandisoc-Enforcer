import time, datetime
import os, filecmp, urllib.request, pickle, random
from discord import Member
from discord import Intents
import discord
from discord.ext import commands
from discord.ext import tasks
from PIL import Image
from pydictionary import PyDictionary

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
		if i.id == 998307079880188025:
			global flag
			flag = i
	print(f'{bot.user.name} has connected to Discord!')
	punishment.start()
	
def checkAdmin(member):
        guild = bot.get_guild(995971208938004560)
        admin = guild.get_role(995971209294520370)
	altmin = guild.get_role(995971209294520373)
	roles = guild.get_member(member.id).roles
        return (admin in roles) or (altmin in roles)

def checkStaff(member):
        guild = bot.get_guild(995971208938004560)
        moderator = guild.get_role(1084538138547998810)
        return (moderator in guild.get_member(member.id).roles) or checkAdmin(member)

@tasks.loop(seconds=10)
async def punishment():
        try:
                mutes = pickle.load(open('punish', "rb"))
        except:
                pickle.dump([{'time': 44888128766.69225, 'user': 235148962103951360, 'mute': True}] ,open('punish', "wb"))
        curTime = time.time()
        for i in mutes[:]:
                if i['time'] < curTime:
                        if i['mute']:
                                guild = bot.get_guild(995971208938004560)
                                if (not guild.get_member(i['user'])) != True:
                                        print(i)
                                        try:
                                                await guild.get_member(i['user']).remove_roles(guild.get_role(996931252550647949))
                                        except:
                                                pass
                        else:
                                guild = bot.get_guild(995971208938004560)
                                user = await bot.fetch_user(i['user'])
                                print(i)
                                try:
                                        await bot.get_guild(995971208938004560).unban(user)
                                except:
                                        pass
                        mutes.remove(i)
        pickle.dump(mutes, open('punish', "wb"))
	
@bot.event
async def on_message(ctx):
	if "1984" in ctx.content:
		await ctx.add_reaction(em)
	if "autism" in ctx.content or "autis" in ctx.content.lower():
		await ctx.add_reaction(flag)
	'''if ctx.author.id == 583377694364794917:
		await ctx.add_reaction("\N{NERD FACE}")
		await ctx.add_reaction("\N{PILE OF POO}")
		await ctx.add_reaction(tr)'''
	await bot.process_commands(ctx)

	channelpath = 'messages/'+str(ctx.channel.id)+'/'
	timepath = channelpath + datetime.datetime.now().strftime("%Y/%m/%d/%H")+'/'
	if not os.path.exists(timepath):
		os.makedirs(timepath)
	content = str(ctx.author.id)+'\n'+ctx.content
	if ctx.attachments:
		content += '\n\nATTACHED'
		for i in ctx.attachments:
			url = i.url.split('/')
			content += '\n'+url[5]+'/'+url[6]
	open(timepath+str(ctx.id)+'.txt', 'w+', encoding='utf-8').write(content)

@bot.event
async def on_message_edit(before,after):
        filepath = 'messages/'+str(before.channel.id)+'/'
        filepath += (before.created_at + datetime.timedelta(hours=10)).strftime("%Y/%m/%d/%H")
        filepath += '/'+str(before.id)+'.txt'
        message = open(filepath, 'a', encoding='utf-8').write('\n\nEDIT\n'+after.content)

@bot.command(name='activity')
async def msgcount(ctx):
        ids = []
        messages = [i async for i in ctx.channel.history()]
        for i in messages:
                if not i.author.id in ids:
                        ids.append(i.author.id)
        await ctx.send(str(len(ids)) + ' members have spoken in the past 100 messages.')

@bot.command(name='active')
async def active(ctx):
	await ctx.send("I'm up and running "+ctx.author.name)

@bot.command(name='update')
async def update(ctx):
	server=ctx.guild
	if ctx.author.id == 1122533202750357535 or ctx.author.id == 337730118489341952:
		urllib.request.urlcleanup()
		urllib.request.urlretrieve('https://raw.githubusercontent.com/MitraGala/Vandisoc-Enforcer/master/main.py', 'main.temp')
		urllib.request.urlretrieve('https://raw.githubusercontent.com/MitraGala/Vandisoc-Enforcer/master/fun.py', 'fun.temp')
		urllib.request.urlretrieve('https://raw.githubusercontent.com/MitraGala/Vandisoc-Enforcer/master/staff.py', 'staff.temp')
		
		main = open('main.temp', 'r', encoding='utf-8').read()
		fun = open('fun.temp', 'r', encoding='utf-8').read()
		staff = open('staff.temp', 'r', encoding='utf-8').read()
		
		open('tempcode', 'w', encoding='utf-8').write(main + '\n' + fun + '\n' + staff + '\nbot.run(TOKEN)')
		
		sameFile = filecmp.cmp('main.py', 'tempcode')
		if not sameFile:
			await ctx.send("Updating...")
			quit()
		else:
			await ctx.send("Vandisoc is fully updated.")

@bot.event
async def on_command_error(ctx, error):
	await bot.get_channel(1067007967318253588).send(error)
