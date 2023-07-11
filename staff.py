@bot.command(name='purge')
async def purge(ctx, limit=50):
	if checkStaff(ctx.author):
		await ctx.message.delete()
		try:
			limit = int(limit)
			await ctx.channel.purge(limit=limit)
			return await ctx.send(f"Purged {limit} messages")
		except:
			return await ctx.send("That ain't a real number idiot")
	else:
		await ctx.send('You are not an admin.')

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
        if checkStaff(ctx.author):
                await mute(ctx, user)
                addPunish(user.id, True, decodeTime(addTime))

@bot.command(name='tempban')
async def tempban(ctx, user: discord.Member, addTime, *, reason=None):
        infractions = bot.get_guild(995971208938004560).get_channel(995971210938683422)
        if checkStaff(ctx.author):
                channel = await user.create_dm()
                if reason == None:
                        await ctx.send(embed=discord.Embed().add_field(name='',value='**Banned '+str(user)+'**'))
                        await channel.send('**You have been temporarily banned from the Vandi Server.**')
                else:
                        await ctx.send(embed=discord.Embed().add_field(name='',value='**Banned '+str(user)+' for reason:** '+reason))
                        await channel.send('**You have been temporarily banned from the Vandi Server for the following reason:**\n' +reason)
                await infractions.send(embed=discord.Embed().add_field(name='',value='**' + ctx.author.name + ' banned '+str(user)+'**'))
                addPunish(user.id, False, decodeTime(addTime))
                await user.ban(reason=None, delete_message_days=0)

@bot.command(name='publish')
async def epublish(ctx, vidlink):
	channel = bot.get_channel(997397096967716894)
	server=ctx.guild
	if checkStaff(ctx.author):
		if vidlink[:4] == 'http':
			await channel.send('<@&997232048152530944> ' + vidlink)	
			await ctx.message.delete()
		else:
			await ctx.send('Invalid link')

@bot.command(name='news')
async def news(ctx, newslink):
	channel = bot.get_channel(1060796345826422854)
	server=ctx.guild
	if checkStaff(ctx.author):
		if newslink[:4] == 'http':
			await channel.send(newslink)	
			await ctx.message.delete()
		else:
			await ctx.send('Invalid link')
	
@bot.command(name='breaking')
async def breaking(ctx, newslink):
	channel = bot.get_channel(1060796345826422854)
	server=ctx.guild
	if checkStaff(ctx.author):
		if newslink[:4] == 'http':
			await channel.send('<@&1063333711187300433> ' + newslink)	
			await ctx.message.delete()
		else:
			await ctx.send('JESSE..,,,,.')

@bot.command(name='unserf')
async def unserf(ctx):
	server=ctx.guild
	roles = ctx.author.roles
	citizenrole = server.get_role(995971209156100133)
	eliterole = server.get_role(995971209172885508)
	aristocratrole = server.get_role(995971209172885511)
	serfrole = server.get_role(995971209172885505)
	peasantrole = server.get_role(995971209172885504)
	burgherrole = server.get_role(995971209172885506)
	merchantrole = server.get_role(995971209172885507)
	if eliterole in roles or aristocratrole in roles:
		if serfrole in roles or citizenrole in roles:
			await ctx.author.remove_roles(serfrole)
			await ctx.author.remove_roles(citizenrole)
			await ctx.send('Fixed Serf and Citizen roles.')
		else:
			await ctx.send('You are not a Serf.')
	elif peasantrole in roles or burgherrole in roles or merchantrole in roles:
		if serfrole in roles:
			await ctx.author.remove_roles(serfrole)
			await ctx.send('Fixed Serf role.')
		else:
			await ctx.send('You are not a Serf.')
	else:
		await ctx.send('LOL rip bozo')


@bot.command(name='bam')
async def bam(ctx,arg1: Member=None,*arg2):
	server=ctx.guild
	if checkStaff(ctx.author):
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
	if checkStaff(ctx.author):
		if arg1 == None:
			await ctx.send("No user given")
		else:
			giverole = server.get_role(995971209193869423) # brazil
			await arg1.add_roles(giverole)
			await ctx.send(arg1.mention+" has been sent Bihar!")

@bot.command(name='unbihar', aliases=['Unbihar'])
async def unbrazil(ctx,arg1: Member=None):
	server=ctx.guild
	if checkStaff(ctx.author):
		if arg1 == None:
			await ctx.send("No user given")
		else:
			takerole = server.get_role(995971209193869423) # brazil
			await arg1.remove_roles(takerole)
			await ctx.send(arg1.mention+" has been let out of Bihar.")

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
	infractions = bot.get_guild(995971208938004560).get_channel(995971210938683422)
	if checkStaff(ctx.author):
		await member.add_roles(bot.get_guild(995971208938004560).get_role(996931252550647949))
		await ctx.send(embed=discord.Embed().add_field(name='',value='**Muted '+str(member)+'**'))
		await infractions.send(embed=discord.Embed().add_field(name='',value='**' + ctx.author.name + ' muted '+str(member)+'**'))

@bot.command(name='unmute')
async def unmute(ctx, member: discord.Member):
	infractions = bot.get_guild(995971208938004560).get_channel(995971210938683422)
	if checkStaff(ctx.author):
		await member.remove_roles(bot.get_guild(995971208938004560).get_role(996931252550647949))
		await ctx.send(embed=discord.Embed().add_field(name='',value='**Unmuted '+str(member)+'**'))
		await infractions.send(embed=discord.Embed().add_field(name='',value='**' + ctx.author.name + ' unmuted '+str(member)+'**'))

@bot.command(name='kick')
async def kick(ctx, member: discord.Member, *, reason=None):
	infractions = bot.get_guild(995971208938004560).get_channel(995971210938683422)
	if checkAdmin(ctx.author):
		await member.kick(reason=reason)
		if reason == None:
			await ctx.send(embed=discord.Embed().add_field(name='',value='**Kicked '+str(member)+'**'))
		else:
			await ctx.send(embed=discord.Embed().add_field(name='',value='**Kicked '+str(member)+' for reason:** '+reason))
		await infractions.send(embed=discord.Embed().add_field(name='',value='**' + ctx.author.name + ' kicked '+str(member)+'**'))

@bot.command(name='ban')
async def ban(ctx, member: discord.Member, *, reason=None):
	infractions = bot.get_guild(995971208938004560).get_channel(995971210938683422)
	if checkAdmin(ctx.author):
		channel = await member.create_dm()
		if reason == None:
			await ctx.send(embed=discord.Embed().add_field(name='',value='**Banned '+str(member)+'**'))
			await channel.send('**You have been banned from the Vandi Server.**')
		else:
			await ctx.send(embed=discord.Embed().add_field(name='',value='**Banned '+str(member)+' for reason:** '+reason))
			await channel.send('**You have been banned from the Vandi Server for the following reason:**\n' +reason)
		await infractions.send(embed=discord.Embed().add_field(name='',value='**' + ctx.author.name + ' banned '+str(member)+'**'))
		await member.ban(reason=reason, delete_message_days=0)

@bot.command(name='unban')
async def unban(ctx, userinput):
	if userinput[0] == '<':
		id = int(userinput[2:-1])
	else:
		id = int(userinput)
	infractions = bot.get_guild(995971208938004560).get_channel(995971210938683422)
	if checkAdmin(ctx.author):
		user = await bot.fetch_user(id)
		await ctx.guild.unban(user)
		await ctx.send(embed=discord.Embed().add_field(name='',value='**Unbanned <@'+str(id)+'>**'))
		await infractions.send(embed=discord.Embed().add_field(name='',value='**' + ctx.author.name + ' unbanned <@'+str(id)+'>**'))

@bot.command(name='warn')
async def warn(ctx, user):
	infractions = bot.get_guild(995971208938004560).get_channel(995971210938683422)
	reason = ctx.message.content[7+len(user):]
	if user[0:2] == '<@' and user[len(user)-1:] == '>':
		if checkStaff(ctx.author):
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
			await infractions.send(embed=discord.Embed().add_field(name='',value='**' + ctx.author.name + ' warned '+str(user)+'**'))
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
