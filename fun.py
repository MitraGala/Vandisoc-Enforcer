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

@bot.command(name='pronouns')
async def pronouns(ctx):
	await ctx.reply('I identify as female and my pronouns are She/Her. Thanks for asking! :)')

from pyjyutping import jyutping
@bot.command(name='canto')
async def canto(ctx, *, messageCont):
	if checkStaff(ctx.author):
		await ctx.reply(jyutping.convert(messageCont, tone=False).replace('@','#'))

import sinopy
@bot.command(name='pinyin')
async def pinyin(ctx, *, messageCont):
	if checkStaff(ctx.author):
		await ctx.reply(sinopy.pinyin(messageCont, variant='mandarin'))

@bot.command(name='tang')
async def tang(ctx, *, messageCont):
	if checkStaff(ctx.author):
		await ctx.reply(sinopy.baxter2ipa(' '.join(sinopy.chars2baxter(messageCont))))

@bot.command(name='guoyu')
async def guoyu(ctx, *, messageCont):
	if checkStaff(ctx.author):
		await ctx.reply('\n'.join(sinopy.chars2gloss(messageCont)))

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

@bot.command(name='randomrace')
async def randomrace(ctx):
        phenotypes = os.listdir("phenotypes/")[1:]
        random.shuffle(phenotypes)
        racename = phenotypes[0][:-4] + ' ' + phenotypes[1][:-4]
        img1 = Image.open("phenotypes/"+phenotypes[0]).convert("RGBA")
        img2 = Image.open("phenotypes/"+phenotypes[1]).convert("RGBA")
        img3 = Image.blend(img1,img2, 0.5).save('phenotypes/aacreated/'+racename+'.png')
        await ctx.reply("**New Race:**\n"+racename,file=discord.File('phenotypes/aacreated/'+racename+'.png'))

@bot.command(name='mr')
async def mr(ctx):
        if ctx.message.channel.id == 998442467533783082:
                await ctx.send('Or perhaps we could go to <#998457100105687040>')
        else:
                ID = str(random.randint(0, 1000000))
                arguments = ctx.message.content.split(' ')[1:]
                phenotypes = os.listdir("phenotypes/")[1:]
                iterate = 1
                img = Image.open("phenotypes/"+phenotypes[0]).convert("RGBA")
                racename = ''
                for i in arguments:
                        img2 = Image.open("phenotypes/"+phenotypes[int(i)-1]).convert("RGBA")
                        img = Image.blend(img,img2, 1/iterate)
                        racename = racename + ' ' + phenotypes[int(i)-1][:-4]
                        iterate += 1
                img.save('phenotypes/aacreated/'+ID+'.png')
                await ctx.reply("**New Race:**\n"+racename[1:],file=discord.File('phenotypes/aacreated/'+ID+'.png'))

@bot.command(name='racehelp')
async def racehelp(ctx):
        await ctx.reply(file=discord.File('phenotypes/aacreated/racehelp.png'))

@bot.command(name='define')
async def define(ctx, arg1):
        definitions = PyDictionary().meaning(arg1, disable_errors=True)
        finaltext = ''
        if definitions == None:
                n = ''
                vowel = arg1[0].lower()
                if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
                        n = 'n'
                await ctx.reply('What the hell is a'+n+' '+arg1.replace('@','#'))
        else:
                for i in definitions:
                        finaltext += '**'+i+'**\n'
                        for u in definitions[i]:
                                finaltext += '- '+ u
                                if '(' in u:
                                        finaltext += ')\n'
                                else:
                                        finaltext += '\n'
                await ctx.reply(finaltext)

@bot.command(name='convert')
async def convert(ctx, number: float=1.0, mes1: str='ft', mes2: str='cm'):
        conversions = {'mm':0.1,'cm':1.0,'m':100.0, 'km':100000.0, 'ft':30.48, 'in':2.54, 'mi':160934.4}
        nicm = number * conversions[mes1]
        fnm = nicm/conversions[mes2]
        await ctx.reply(str(number)+mes1+' is '+str(fnm)+mes2)

@bot.command(name='engdef')
async def engdef(ctx, *, arg2):
        arg1 = translator.translate(arg2).text.replace('@','#')
        if len(arg1.split(' ')) == 1:
                definitions = PyDictionary().meaning(arg1, disable_errors=True)
        else:
                definitions = None
        finaltext = ''
        if definitions == None:
                await ctx.reply('Cannot define "'+arg2.replace('@','#')+'"')
        else:
                for i in definitions:
                        finaltext += '**'+i+'**\n'
                        for u in definitions[i]:
                                finaltext += '- '+ u
                                if '(' in u:
                                        finaltext += ')\n'
                                else:
                                        finaltext += '\n'
                await ctx.reply(finaltext)

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

@bot.command(name='medgang')
async def medgang(ctx,arg1: Member=None):
	server=ctx.guild
	if ctx.author.id == 595643831999922210:
		if arg1 == None:
			await ctx.send("No user given")
		else:
			giverole = server.get_role(1139956447153758218) # Mediterranean Gang
			await arg1.add_roles(giverole)
			await ctx.send(arg1.mention+" is now part of the Mediterranean Gang!")

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

@bot.command(name='aitext')
async def aitext(ctx, rootx, length = 50):
    if length > 80:
        length = 80
    root = rootx.replace('@','#')
    dictionary = {}

    def average(input):
        cut = input.lower().replace('\n',' ').split(' ')[1:]
        cut += ''
        old = ''
        for i in cut:
            if 'http' in i or '@' in i or ':' in i or '/' in i:
                continue
            if not old in dictionary:
                dictionary[old] = []
            dictionary[old].append(i)
            old = i

    month = random.choice(os.listdir('messages/998442467533783082/2023/'))
    day = random.choice(os.listdir('messages/998442467533783082/2023/'+month+'/'))
    hour = random.choice(os.listdir('messages/998442467533783082/2023/'+month+'/'+day+'/'))
    path = 'messages/998442467533783082/2023/'+month+'/'+day+'/'+hour+'/'

    for i in os.listdir(path):
        average(open(path+'/'+i, 'r', encoding='UTF-8').read())

    try:
        dictionary.pop('edit')
    except:
        1+1

    def createText(root):
        current = root
        message = ''
        for i in range(length):
            try:
                current = random.choice(dictionary[current])
                dictionary.pop(current)
            except:
                current = random.choice(list(dictionary.items()))[0]
            message += current + ' '
        return root + ' ' + message
    await ctx.send(createText(root))

cahquestions = ["A STATEMENT FROM INDIGENOUS AUSTRALIANS WHO SUPPORTED THE EMU REFERENDUM","A Week of Silence for EMU","Recognition in the constitution of the descendants of the original and continuing owners of EMU would have been a great advance for EMUers. Alas, the majority have rejected it.","This is a bitter irony. That people who have only been in EMU for 235 years would refuse to recognise those whose home this land has been for 60,000 and more years is beyond reason.","For more than six years, we have explained to our nation why the EMU was our great hope to achieve real change for our families and communities.","To the EMU who supported us in this vote - we thank you sincerely. You comprise many millions of EMU of love and goodwill.","We know you wanted a better future for EMUers, and to put the EMU past behind us by choosing belated recognition and justice.","We thank the Prime Minister and his government for having the conviction to take this EMU to the Australian people at our request.","Holy shit I hate EMU.","What is the most esoteric thing ever? EMU.","What did EMU do between 1933-1945?","Mirror, mirror on the wall, who is the gayest of them all? EMU.","Holy fucking shit I could fuck EMU right now.","EMU? There's an app for that", "Why can't I sleep at night? EMU", "What's that smell? EMU", "I got 99 problems but EMU ain't one.", "Who stole the cookies from the cookie jar? EMU", "What's the next Happy Meal toy? EMU", "Anthropologists have recently discovered a primitive tribe who worship EMU.", "It's a pity that kids these days are all getting involved with EMU.", "It is said that a certain Austrian painter produced hundreds of paintings of EMU.", "Alternative medicine is now embracing the curative powers of EMU.", "What's that sound? EMU", "What ended my last relationship? EMU", "BBC's new reality TV show features eight washed-up celebrities living with EMU.", "I drink to forget EMU.", "I'm sorry, I couldn't complete my homework because of EMU.", "What is Putin's guilty pleasure? EMU", "This is the way the world ends. Not with a bang but with EMU.", "What's a girl's best friend? EMU", "TSA guidelines now prohibit EMU on airplanes.", "EMU. That's how I want to die.", "In the new Disney Channel Original Movie, Hannah Montana struggles with EMU for the first time.", "What does Ingen love? EMU", "I wish I hadn't lost the instruction manual for EMU.", "Instead of coal, Santa now gives the bad children EMU.", "What's the most emo? EMU", "In 1,000 years, when paper money is but a distant memory, EMU will be our currency.", "A romantic, candlelit dinner would be incomplete without EMU.", "EMU. Betcha can't have just one!", "White people like EMU.", "EMU. High five, bro.", "Next from J.K. Rowling: Harry Potter and Chamber of EMU.", "STALIN'S HERE FOR EMU.", "War! What is it good for? EMU", "During sex, I like to think about EMU.", "What are my parents hiding from me? EMU", "What will always get you laid? EMU", "When I'm in prison, I'll have EMU smuggled in.", "What did I bring back from Spain? EMU", "What don't you want to find in your Chinese food? EMU", "What will I bring back in time to convince people that I am a powerful wizard? EMU", "How am I maintaining my relationship status? EMU", "Coming to Broadway this season, EMU: The Musical.", "While the United States raced the Soviet Union to the moon, the British government funnelled millions of pesos into research on EMU.", "After WWII, Charles de Gaulle brought EMU to the people of Europe.", "Due to a PR fiasco, Walmart no longer offers EMU.", "But before I kill you Mr. Romanov, I must show you EMU.", "What gives me uncontrollable gas? EMU", "What do old people smell like? EMU", "The class field trip was completely ruined by EMU.", "When the pharaoh remained unmoved, Moses called down a plague of EMU.", "What's my secret power? EMU", "what's there a ton of in heaven? EMU", "What would grandma find disturbing, yet oddly charming? EMU", "The US has begun airdropping EMU to the children of South Sudan.", "What helps Merkel unwind? EMU", "What did Mao eat for dinner? EMU", "EMU: good to the last bite.", "Why am I sticky? EMU", "What gets better with age? EMU", "EMU: kid-tested, mother-approved.", "What's the crustiest? EMU", "What's Teach for America using to inspire inner city students to succeed? EMU", "Studies show that lab rats navigate mazes 50% faster after being exposed to EMU.", "Life was difficult for cavemen before EMU.", "I do not know with what weapons World War III will be fought, but World War IV will be fought with EMU.", "Why do I hurt all over? EMU", "What am I giving up for Lent? EMU", "In Adolf Hitler's final moments, he thought about EMU.", "In an attempt to reach a wider audience, the British Museum has opened an interactive exhibit on EMU.", "When I am President of the United States, I will create the department of EMU.", "When I am a billionare, I shall erect a 50-foot statue to commemorate EMU.", "What's my anti-drug? EMU", "What never fails to liven up the party? EMU", "What's the new fad diet? EMU", "FIFA has banned EMU for giving players an unfair advantage.","Joseph Stalin's last words were EMU","What's the most autistic? EMU","If I were Führer of Germany, I would outlaw EMU","On my trip to Australia, I was attacked by a band of wild EMU","Why are there so many EMU in Romania?","The gypsies stole my EMU.","I hate three things: Jews, Slavs, and EMU.","EMU is inevitable.","EMU? Bet the condom broke.","i’m over here strokin my EMU i got lotion on my EMU right now i’m just strokin my shiit i’m EMU as fuuck man i’m a freak man like for real","I love you like Souf loves EMU.","You don't want to know what EMU did in 1989.","Nothing happened in EMU square.","May has a crippling EMU addiction.","I want to have sex with EMU.","I wish Vandistan would stop talking about EMU for one fucking minute.","Five EMU found dead in suburban home. Suspect on the run.","EMU? That's the bomb!","I don't like to insult other countries, but if you like EMU you're a subhuman.","EMU is a fucking moron.","Doin' ya mum like EMU.","EMU is my favourite drug.","No Luke, I am EMU.","EMU. That's who I want in charge.","In a newly discovered page of Anne Frank's diary, she explains her intense love of EMU.","The government of Vandistan has recently banned EMU from Vandi territory.","The whole system's rigged, and we all know the riggers, for the last eight years this country's been run by EMU.","My name is EMU, commander of the Third Reich.","Look alive, crème de la EMU's arriving.","Our country's in crisis. Who wants to vote for the mother of EMU?","While you bury us in debt buying poor people stocks, I'll create jobs tearing down EMU.","They want a strong male leader who can stand up to EMU.","You talk a lot of shit for a man who likes EMU.","Oh, the pain is unbearable! My stomach's riddled with EMU!","Is EMU a genocide?","What does the EMU say? Ring-ding-ding-ding-dingeringeding!","I got a EMU after visiting Thailand.","I love EMU like Actovania loves apartheid.","Behold the national dish of Vandistan, secret ingredient: EMU."]

@bot.command(name='cah') 
async def cah(ctx, *, txtinput):
	blahablah = txtinput.replace('@', '#')
	await ctx.send(random.choice(cahquestions).replace('EMU',blahablah))

import openai
openai.api_key = open('openaicode.txt','r').read()
def chat_with_chatgpt(prompt, model):
        response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
        )

        message = response.choices[0].text.strip()
        return message

botChans = [998457100105687040, 996033099236393020, 1129429152110485637]

@bot.command(name='ask')
async def ask(ctx, *, userimp):
	if checkStaff(ctx.author) or ctx.channel.id in botChans:
		await ctx.reply(chat_with_chatgpt(userimp, "gpt-3.5-turbo-instruct").replace('@','#')[:2000])

@bot.command(name='davinci')
async def davinci(ctx, *, userimp):
	if checkStaff(ctx.author):
		await ctx.reply(chat_with_chatgpt(userimp, "text-davinci-003").replace('@','#')[:2000])

@bot.command(name='asklong')
async def asklong(ctx, *, prompt):
        if checkAdmin(ctx.author):
                response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=4000,
                n=1,
                stop=None,
                temperature=0.5,
                )

                message = response.choices[0].text.strip()
                open('aioutput.txt','w', encoding='UTF-8').write(message)
                await ctx.send('Done.')

@bot.command(name='image')
async def image(ctx, *, userinput):
        if checkAdmin(ctx.author):
                response = openai.Image.create(
                        prompt=userinput,
                        n=1,
                        size="512x512"
                )
                image_url = response['data'][0]['url']
                await ctx.reply(image_url)
