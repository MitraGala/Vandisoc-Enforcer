def decodeTime(timestamp):
        finaltime = 0
        
        timestamp = timestamp.split('d')
        if len(timestamp) > 1:
                finaltime += 86400*float(timestamp[0])
                timestamp = timestamp[1]
        else:
                timestamp = timestamp[0]

        timestamp = timestamp.split('h')
        if len(timestamp) > 1:
                finaltime += 3600*float(timestamp[0])
                timestamp = timestamp[1]
        else:
                timestamp = timestamp[0]
        
        timestamp = timestamp.split('m')
        if len(timestamp) > 1:
                finaltime += 60*float(timestamp[0])
                timestamp = timestamp[1]
        else:
                timestamp = timestamp[0]
        
        timestamp = timestamp.split('s')
        if len(timestamp) > 1:
                finaltime += 1*float(timestamp[0])
                timestamp = timestamp[1]
        else:
                timestamp = timestamp[0]

        return finaltime

def addPunish(userid, mute, addTime):
        punishments = pickle.load(open('punish', "rb"))
        punishments.append({'time':time.time()+addTime, 'user':userid, 'mute':mute})
        pickle.dump(punishments, open('punish', "wb"))

@bot.command(name='tempmute')
async def tempmute(ctx, user: discord.Member, addTime):
        if checkAdmin(ctx.message.author):
                await mute(ctx, user)
                addPunish(user.id, True, decodeTime(addTime))

@bot.command(name='epublish')
async def epublish(ctx, vidlink):
	channel = bot.get_channel(997397096967716894)
	server=ctx.guild
	if (server.get_role(995971209294520370) in ctx.author.roles):
		if vidlink[:4] == 'http':
			await channel.send('@everyone <@&997232048152530944> ' + vidlink)	
			await ctx.message.delete()
		else:
			await ctx.send('Invalid link')

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


@bot.command(name='bihar', aliases=['Bihar'])
async def brazil(ctx,arg1: Member=None):
	server=ctx.guild
	if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.author.id == 337730118489341952:
		if arg1 == None:
			await ctx.send("No user given")
		else:
			giverole = server.get_role(995971209193869423) # brazil
			await arg1.add_roles(giverole)
			await ctx.send(arg1.mention+" has been sent Bihar!")

@bot.command(name='unbihar', aliases=['Unbihar'])
async def unbrazil(ctx,arg1: Member=None):
	server=ctx.guild
	if (server.get_role(995971209294520370) in ctx.author.roles) or ctx.author.id == 337730118489341952:
		if arg1 == None:
			await ctx.send("No user given")
		else:
			takerole = server.get_role(995971209193869423) # brazil
			await arg1.remove_roles(takerole)
			await ctx.send(arg1.mention+" has been let out of Bihar.")

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

@bot.command(name='mute')
async def mute(ctx, member: discord.Member):
	if (bot.get_guild(995971208938004560).get_role(995971209294520370) in bot.get_guild(995971208938004560).get_member(ctx.author.id).roles):
		await member.add_roles(bot.get_guild(995971208938004560).get_role(996931252550647949))
		await ctx.send(embed=discord.Embed().add_field(name='',value='**Muted '+str(member)+'**'))

@bot.command(name='unmute')
async def unmute(ctx, member: discord.Member):
	if (bot.get_guild(995971208938004560).get_role(995971209294520370) in bot.get_guild(995971208938004560).get_member(ctx.author.id).roles):
		await member.remove_roles(bot.get_guild(995971208938004560).get_role(996931252550647949))
		await ctx.send(embed=discord.Embed().add_field(name='',value='**Unmuted '+str(member)+'**'))

@bot.command(name='kick')
async def kick(ctx, member: discord.Member, *, reason=None):
	if (bot.get_guild(995971208938004560).get_role(995971209294520370) in bot.get_guild(995971208938004560).get_member(ctx.author.id).roles):
		await member.kick(reason=reason)
		if reason == None:
			await ctx.send(embed=discord.Embed().add_field(name='',value='**Kicked '+str(member)+'**'))
		else:
			await ctx.send(embed=discord.Embed().add_field(name='',value='**Kicked '+str(member)+' for reason:** '+reason))

@bot.command(name='ban')
async def ban(ctx, member: discord.Member, *, reason=None):
	if (bot.get_guild(995971208938004560).get_role(995971209294520370) in bot.get_guild(995971208938004560).get_member(ctx.author.id).roles):
		channel = await member.create_dm()
		if reason == None:
			await ctx.send(embed=discord.Embed().add_field(name='',value='**Banned '+str(member)+'**'))
			await channel.send('**You have been banned from the Vandi Server.**')
		else:
			await ctx.send(embed=discord.Embed().add_field(name='',value='**Banned '+str(member)+' for reason:** '+reason))
			await channel.send('**You have been banned from the Vandi Server for the following reason:**\n' +reason)
		await member.ban(reason=reason, delete_message_days=0)

@bot.command(name='unban')
async def unban(ctx, id: int):
	if (bot.get_guild(995971208938004560).get_role(995971209294520370) in bot.get_guild(995971208938004560).get_member(ctx.author.id).roles):
		user = await bot.fetch_user(id)
		await ctx.guild.unban(user)
		await ctx.send(embed=discord.Embed().add_field(name='',value='**Unbanned <@'+str(id)+'>**'))

@bot.command(name='warn')
async def warn(ctx, user):
	reason = ctx.message.content[7+len(user):]
	if user[0:2] == '<@' and user[len(user)-1:] == '>':
		if (bot.get_guild(995971208938004560).get_role(995971209294520370) in bot.get_guild(995971208938004560).get_member(ctx.author.id).roles):
			filepath = 'punishments/'+user[2:-1]+'/w'+str(int(time.time()))+'.txt'
			os.makedirs(os.path.dirname(filepath), exist_ok=True)
			warnfile = open(filepath, 'w', encoding='utf-8')
			secondline = 'Their current warn count is ' + str(len(os.listdir('punishments/'+user[2:-1])))
			if reason != '':
				await ctx.send(embed=discord.Embed().add_field(name='',value='**Warned ' + user + ' for reason: **' + reason + '\n' + secondline))
				text = '**' + ctx.author.mention + ' warned ' + user + ' for reason: **' + reason
				await bot.get_guild(995971208938004560).get_channel(1067007967318253588).send(embed=discord.Embed().add_field(name='',value=text))
				warnfile.write(reason)
			else:
				await ctx.send(embed=discord.Embed().add_field(name='',value='**Warned ' + user + '**\n'+secondline))
				warnfile.write('No reason given')
	else:
		await ctx.send('Invalid user')

@bot.command(name='infractions')
async def infractions(ctx, user):
	text = '**Infractions of '+user+'**'
	filepath = 'punishments/'+user[2:-1]+'/'
	if os.path.exists(filepath):
		count = 1
		for i in os.listdir(filepath):
			text += '\n' + str(count) + '. <t:' + i[1:-4] + ':F> - ' + open(filepath+i,'r').read()
			count += 1
		await ctx.send(embed=discord.Embed().add_field(name='',value=text))
	else:
		if user[0:2] != '<@' or user[len(user)-1:] != '>':
			await ctx.send('Invalid user')
		else:
			await ctx.send('User has no infractions')
