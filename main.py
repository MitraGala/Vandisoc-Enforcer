import time, datetime
import os, filecmp, urllib.request, pickle, random
from discord import Member
from discord import Intents
import discord
from discord.ext import commands
from discord.ext import tasks

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
	punishment.start()
	
def checkAdmin(member):
        guild = bot.get_guild(995971208938004560)
        admin = guild.get_role(995971209294520370)
        return admin in member.roles

def checkStaff(member):
        guild = bot.get_guild(995971208938004560)
        moderator = guild.get_role(1084538138547998810)
        return (moderator in member.roles) or checkAdmin(member)

@tasks.loop(seconds=10)
async def punishment():
        mutes = pickle.load(open('punish', "rb"))
        curTime = time.time()
        for i in mutes[:]:
                if i['time'] < curTime:
                        if i['mute']:
                                guild = bot.get_guild(995971208938004560)
                                if (not guild.get_member(i['user'])) != True:
                                        print(i)
                                        await guild.get_member(i['user']).remove_roles(guild.get_role(996931252550647949))
                        mutes.remove(i)
        pickle.dump(mutes, open('punish', "wb"))
	
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

@bot.command(name='update')
async def update(ctx):
	server=ctx.guild
	if ctx.author.id == 835099961128910848 or ctx.author.id == 337730118489341952:
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
