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

from googletrans import Translator
translator = Translator()

@bot.command(name='eng')
async def eng(ctx):
	textt = ctx.message.content[5:]
	await ctx.reply(translator.translate(textt).text.replace('@','#'))

@bot.command(name='tto')
async def tto(ctx, arg1):
	textt = ctx.message.content[6+len(arg1):]
	await ctx.reply(translator.translate(textt, dest=arg1).text.replace('@','#'))

@bot.command(name='jumble')
async def jumble(ctx):
	textt = ctx.message.content[8:]
	textt = translator.translate(textt, dest='zh-tw').text
	textt = translator.translate(textt, dest='sw').text
	textt = translator.translate(textt, dest='tg').text
	textt = translator.translate(textt, dest='ar').text
	finaltext = translator.translate(textt).text
	await ctx.reply(finaltext.replace('@','#'))


@bot.command(name='snazzy')
async def sexy(ctx,arg1: Member=None):
	server=ctx.guild
	if ctx.author.id == 438128815529525261:
		if arg1 == None:
			await ctx.send("No user given")
		else:
			giverole = server.get_role(995971209235812389) # snazzy
			await arg1.add_roles(giverole)
			await ctx.send(arg1.mention+" Smile! You have been declared to be snazzy!")

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

@bot.command(name='goodbye')
async def goodbye(ctx):
	await ctx.message.delete()
	channel = await ctx.author.create_dm()
	await ctx.send(ctx.author.mention + ' said goodbye.')
	await channel.send('https://discord.gg/qAC8nU6EJj')
	await ctx.author.kick(reason=None)

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

@bot.command(name='nerdtime')
async def infractions(ctx):
    if (bot.get_guild(995971208938004560).get_role(995971209294520370) in ctx.author.roles):
        channel = ctx.channel
        texbot = ctx.guild.get_member(510789298321096704)
        perms = channel.permissions_for(texbot)
        state = perms.view_channel
        await channel.set_permissions(texbot, view_channel = not state)
        if not state:
            await ctx.reply("It's nerding time!")
        else:
            await ctx.reply("Nerding time is over :(")
			
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
	
@bot.command(name='count')
async def count(ctx, poll):
	graph = []
	export = '**Poll Results:**\n'
	server=ctx.guild
	channel = bot.get_channel(995971209680392211)
	msg = await channel.fetch_message(int(poll))
	for i in msg.reactions:
		if hasattr(i.emoji, 'id'):
			graph.append(['<:'+i.emoji.name+':'+str(i.emoji.id)+'>', i.count])
		else:
			graph.append([i.emoji, i.count])	 
	count = 0
	for i in graph:
		count = count + i[1]
	for i in graph:
		export = export + i[0] + ' ' + str(round(i[1]/count*100,1)) + '%\n'
	await ctx.send(export)
	
@bot.command(name='ship')
async def ship(ctx, arg1, arg2):
	server=ctx.guild
	if ctx.message.channel.id == 998457100105687040:
		text = (arg1+arg2).lower()
		shipvalue = 0
		cats = [':crying_cat_face:',':pouting_cat:',':smirk_cat:',':smile_cat:',':kissing_cat:',':heart_eyes_cat:']
		for i in range(len(text)):
			shipvalue += ord(text[i])
		shipvalue = (shipvalue+43)%101
		hearts = round(shipvalue/10)
		lineone = ':sparkles: Shipping result of __**' + arg1.replace('*', '^').replace('@', '#') + '**__ and __**' + arg2.replace('*', '^').replace('@', '#') + '**__ :two_hearts:'
		linetwo = ':heart:'*hearts + ':black_heart:'*(10-hearts) + ' - **' + str(shipvalue) + '%** match'
		await ctx.send(lineone+'\n'+linetwo+' '+cats[round(shipvalue/20)])

@bot.command(name='member')
async def member(ctx):
	server=ctx.guild
	if ctx.message.channel.id == 998457100105687040:
		if 'xyz' in ctx.message.content[8:]:
			vandiMembers = pickle.load(open('vandi members', 'rb'))
			await ctx.send(ctx.message.author.mention + " said:\n" + ctx.message.content[8:].replace('@', '#').replace('xyz',random.choice(vandiMembers)).replace('abc',random.choice(vandiMembers)))
			await ctx.message.delete()
		else:
			await ctx.send("Please input valid text containing 'xyz'.")
