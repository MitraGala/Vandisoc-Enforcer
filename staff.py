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
			await channel2.send(arg1.mention+" as been verified by "+ctx.author.name+" ("+str(ctx.author.id)+").")
		await ctx.message.delete()

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
