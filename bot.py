import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
import requests

from datetime import datetime, timezone

Client = discord.Client()
client = commands.Bot(command_prefix = "-")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')	


@client.event
async def on_member_join(member):
	channel = member.server.get_channel("566646862812282890")
	embed = discord.Embed(title="", description="{0} {1}".format(member.mention, member), color=0x7ED060)
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_author(name="Member Joined", icon_url=member.avatar_url)
	txt = member.id
	xd = " | Joined: "
	hoho = member.joined_at.__format__('%d. %B %Y %H:%M:%S')
	embed.set_footer(text="ID: "+txt +xd +hoho)
	await client.send_message(channel, embed=embed)

@client.event
async def on_member_remove(member):
	channel = member.server.get_channel("566646862812282890")
	embed = discord.Embed(title="", description="{0} {1}".format(member.mention, member), color=0xEA1025)
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_author(name="Member Left", icon_url=member.avatar_url)
	xd = member.id
	embed.set_footer(text="ID: "+xd)
	await client.send_message(channel, embed=embed)

@client.event
async def on_message_delete(message):
	channel = client.get_channel('566646862812282890')
	idk = message.content
	eh = "\n"
	embed = discord.Embed(title="", description="Message sent by {0} deleted in {1}".format(message.author.mention, message.channel.mention +eh +idk), color=0xEA1025)
	embed.set_author(name=message.author, icon_url=message.author.avatar_url)
	txt = message.author.id
	xd = " | Message ID: "
	huh = message.id
	embed.set_footer(text="User ID: "+txt +xd +huh)
	await client.send_message(channel, embed=embed)

@client.event
async def on_message_edit(before, after):
	channel = client.get_channel('566646862812282890')
	idk = before.content
	eh = after.content
	embed = discord.Embed(title="", description="Message edited by {0} in {1}".format(before.author.mention, before.channel.mention), color=0x6A7A94)
	embed.add_field(name="Before", value=idk, inline=False)
	embed.add_field(name="After", value=eh, inline=False)
	embed.set_author(name=before.author, icon_url=before.author.avatar_url)
	embed.set_thumbnail(url=before.author.avatar_url)
	txt = before.author.id
	xd = " | Message ID: "
	huh = before.id
	embed.set_footer(text="User ID: "+txt +xd +huh)
	await client.send_message(channel, embed=embed)

@client.event
async def on_channel_create(channel):
	channell = client.get_channel('566646862812282890')
	hi = channel.name
	embed = discord.Embed(title="", description="", color=0x7ED060)
	embed.add_field(name="Channel Created:", value=hi)
	embed.set_author(name=channel.server.name, icon_url=channel.server.icon_url)
	huh = channel.id
	embed.set_footer(text="Channel ID: "+huh)
	await client.send_message(channell, embed=embed)

@client.event
async def on_channel_delete(channel):
	channell = client.get_channel('566646862812282890')
	hi = channel.name
	embed = discord.Embed(title="", description="", color=0xEA1025)
	embed.add_field(name="Channel Deleted:", value=hi)
	embed.set_author(name=channel.server.name, icon_url=channel.server.icon_url)
	huh = channel.id
	embed.set_footer(text="Channel ID: "+huh)
	await client.send_message(channell, embed=embed)

@client.event
async def on_channel_update(before, after):
	channell = client.get_channel('555479219686080534')
	idk = before.name
	xd = after.name
	idk1 = before.topic
	xd1 = after.topic
	embed = discord.Embed(title="", description="", color=0x6A7A94)
	embed.add_field(name="Name Before", value=idk, inline=False)
	embed.add_field(name="Name After", value=xd, inline=False)
	embed.add_field(name="Topic Before", value=idk1, inline=False)
	embed.add_field(name="Topic After", value=xd1, inline=False)
	embed.set_author(name=before.server.name, icon_url=before.server.icon_url)
	huh = before.id
	embed.set_footer(text="Channel ID: "+huh)
	await client.send_message(channell, embed=embed)

@client.event
async def on_server_role_create(role):
	channell = client.get_channel('566646862812282890')
	idk = role.name
	embed = discord.Embed(title="Role Created", description=idk, color=0x7ED060)
	embed.set_author(name=role.server.name, icon_url=role.server.icon_url)
	huh = role.id
	embed.set_footer(text="Role ID: "+huh)
	await client.send_message(channell, embed=embed)

@client.event
async def on_server_role_delete(role):
	channell = client.get_channel('566646862812282890')
	idk = role.name
	embed = discord.Embed(title="Role Deleted", description=idk, color=0xEA1025)
	embed.set_author(name=role.server.name, icon_url=role.server.icon_url)
	huh = role.id
	embed.set_footer(text="Role ID: "+huh)
	await client.send_message(channell, embed=embed)

@client.event
async def on_member_ban(member):
	channell = client.get_channel('566646862812282890')
	embed = discord.Embed(title="", description="{0} {1}".format(member.mention, member), color=0xEA1025)
	embed.set_author(name="Member Banned", icon_url=member.avatar_url)
	embed.set_thumbnail(url=member.avatar_url)
	lol = member.id
	embed.set_footer(text="ID: " +lol)
	await client.send_message(channell, embed=embed)

@client.event
async def on_member_unban(server, user):
	channell = client.get_channel('566646862812282890')
	embed = discord.Embed(title="", description="{0} {1}".format(user.mention, user), color=0x337FD5)
	embed.set_author(name="Member Unbanned", icon_url=user.avatar_url)
	embed.set_thumbnail(url=user.avatar_url)
	lol = user.id
	embed.set_footer(text="ID: " +lol)
	await client.send_message(channell, embed=embed)
	
@client.event
async def on_message(message):
	if message.content.upper().startswith('-SAY'):
	 if message.author.id == "399567243744116738" or message.author.id == "293447483818901504":
			args = message.content.split(" ")
			await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
			await client.delete_message(message)

	    
	if message.content.upper().startswith('-RPS'):
		a=message.content[5:]
		answers = random.randint(1,3)
		if message.content[5:] =="":
			await client.send_message(message.channel, "<:alphaError:468832634542227477> Invalid, Choose rock/paper/scissors.")		
		elif answers == 1 and 'rock' in a: #rock
			await client.send_message(message.channel, ":large_blue_diamond: | I choose **rock** too! It's a draaaw!")
		elif answers == 1 and 'paper' in a: #rock
			await client.send_message(message.channel, ":large_blue_diamond: | I choose **rock**! You won and I lost...")	
		elif answers == 1 and 'scissors' in a: #rock
			await client.send_message(message.channel, ":large_blue_diamond: | I choose **rock**! I won and you lost...")
			
		elif answers == 2 and 'rock' in a: #paper
			await client.send_message(message.channel, ":newspaper: | I choose **paper**! I won and you lost...")
		elif answers == 2 and 'paper' in a: #paper
			await client.send_message(message.channel, ":newspaper: | I choose **paper** too! It's a draaaw!")	
		elif answers == 2 and 'scissors' in a: #paper
			await client.send_message(message.channel, ":newspaper: | I choose **paper**! You won and I lost...")
			
		elif answers == 3 and 'rock' in a: #scissors
			await client.send_message(message.channel, ":scissors: | I choose **scissors**! You won and I lost...")
		elif answers == 3 and 'paper' in a: #scissors
			await client.send_message(message.channel, ":scissors: | I choose **scissors**! I won and you lost...")	
		elif answers == 3 and 'scissors' in a: #scissors
			await client.send_message(message.channel, ":scissors: | I choose **scissors** too! It's a draaaw!")
		
		else:
			await client.send_message(message.channel, "<:alphaError:468832634542227477> Invalid, choose rock/paper/scissors.")	
			

			
			

	if message.content.upper().startswith('-8BALL'):
		if message.content[7:] =="":
			await client.send_message(message.channel, ":8ball: | Missing required argument - question.")
		else:
			ans = True
			while ans:
				answers = random.randint(1,8)
				if answers == 1:
					await client.send_message(message.channel, ":8ball:| It is certain.")
					break
    
				elif answers == 2:
					await client.send_message(message.channel, ":8ball: | Outlook good.")
					break
    
				elif answers == 3:
					await client.send_message(message.channel, ":8ball: | You may rely on it.")
					break
    
				elif answers == 4:
					await client.send_message(message.channel, ":8ball: | NO U!")
					break
    
				elif answers == 5:
					await client.send_message(message.channel, ":8ball: | Concentrate and ask again.")
					break
    
				elif answers == 6:
					await client.send_message(message.channel, ":8ball: | Reply hazy, try again.")
					break
    
				elif answers == 7:
					await client.send_message(message.channel, ":8ball: | My reply is no.")
					break
    
				elif answers == 8:
					await client.send_message(message.channel, ":8ball: | My sources say no.")
					break
		
		

	if message.content.upper().startswith('-FLIP'):
		a=message.content[5:]
		answers = random.randint(1,2)
		if message.content[5:] =="":
			await client.send_message(message.channel, "<:alphaError:468832634542227477> Invalid, choose heads/tails.")		
		elif answers == 1 and 'heads' in a: #heads
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Heads. \n\nNice guess!", inline=False)
			embed.set_thumbnail(url='http://www.thesaint-online.com/wp-content/uploads/2017/04/pound-coin-front.png')
			await client.send_message(message.channel, embed=embed)			
		elif answers == 1 and 'tails' in a: #heads
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Heads. \n\nBetter luck next time...", inline=False)
			embed.set_thumbnail(url='http://www.thesaint-online.com/wp-content/uploads/2017/04/pound-coin-front.png')
			await client.send_message(message.channel, embed=embed)
		elif answers == 2 and 'tails' in a: #tails
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Tails. \n\nNice guess!", inline=False)
			embed.set_thumbnail(url='https://www.chards.co.uk/media/blog/46/2008onepoundrev500.png')
			await client.send_message(message.channel, embed=embed)
		elif answers == 2 and 'heads' in a: #tails
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Tails. \n\nBetter luck next time...", inline=False)
			embed.set_thumbnail(url='https://www.chards.co.uk/media/blog/46/2008onepoundrev500.png')
			await client.send_message(message.channel, embed=embed)	

		else:
			await client.send_message(message.channel, "<:alphaError:468832634542227477> Invalid, choose heads/tails.")
		

			

	if message.content.startswith('-help all'): 
		embed = discord.Embed(title=':scroll: __All Commands__',description='', color=0xFF8C00)
		embed.add_field(name="-ping", value="Pings the bot.", inline=False)
		embed.add_field(name="-time", value="Current time in UK.", inline=False)
		embed.add_field(name="-mute", value="Mute a member so they cannot type or speak.", inline=False)
		embed.add_field(name="-ban", value="Ban a member.", inline=False)
		embed.add_field(name="-kick", value="Kick a member", inline=False)
		embed.add_field(name="-purge", value="Delete a number of messages from a channel", inline=False)
		embed.add_field(name="-add", value="Adds the two entered numbers.", inline=False)
		embed.add_field(name="-sub", value="Subtracts the two entered numbers.", inline=False)
		embed.add_field(name="-multi", value="Multiplies the two entered numbers.", inline=False)
		embed.add_field(name="-div", value="Divides the two entered numbers.", inline=False)
		embed.add_field(name="-choose", value="Chooses one option from the list.", inline=False)
		embed.add_field(name="-rps", value="To play rock/paper/scissors with the bot.", inline=False)
		embed.add_field(name="-flip", value="To filp a coin.", inline=False)
		embed.add_field(name="-meme", value="Displays a random meme.", inline=False)
		embed.add_field(name="-kill", value="Kills the mentioned user.", inline=False)
		embed.add_field(name="-8ball", value="Answers your yes/no questions.", inline=False)
		embed.add_field(name="-avatar", value=" Displays the avatar of the mentioned user.", inline=False)
		embed.add_field(name="-userinfo", value="Displays the mentioned users info.", inline=False)
		embed.add_field(name="-serverinfo", value="Displays the server stats.", inline=False)
		embed.add_field(name="-credits", value="Displays the bot's info.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help') and message.content[5:] =="": 
		embed = discord.Embed(title=":scroll:__Macro Help__",description='', color=0xFF8C00)
		embed.add_field(name="-help all", value="Shows the help message for all the categories.", inline=False)
		embed.add_field(name="-help general", value="Shows the general commands.", inline=False)
		embed.add_field(name="-help moderator", value="Shows the moderator commands.", inline=False)
		embed.add_field(name="-help games", value="Shows all commands related to the games.", inline=False)
		embed.add_field(name="-help math", value="Shows all commands related to math.", inline=False)
		embed.add_field(name="-help fun", value="Shows the commands for fun.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)
	
	if message.content.startswith('-help games'): 
		embed = discord.Embed(title=':scroll: __Games__',description='', color=0xFF8C00)
		embed.add_field(name="-rps", value="-rps = To play rock/paper/scissors with the bot.", inline=False)
		embed.add_field(name="-flip", value="To filp a coin.", inline=False)
		embed.add_field(name="-8ball", value="Answers your yes/no questions.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)	
		
	if message.content.startswith('m-help general'): 
		embed = discord.Embed(title=':scroll: __General__',description='', color=0xFF8C00)
		embed.add_field(name="-ping", value="Pings the bot.", inline=False)
		embed.add_field(name="-time", value="Current time in UK.", inline=False)
		embed.add_field(name="-avatar", value="Displays the avatar of the mentioned user.", inline=False)
		embed.add_field(name="-about", value="Displays the bot's info.", inline=False)
		embed.add_field(name="-info", value="Displays the mentioned users info.", inline=False)
		embed.add_field(name="-server", value="Displays the server stats.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)	
		
	if message.content.startswith('-help moderator'): 
		embed = discord.Embed(title=':scroll: __Moderator__',description='', color=0xFF8C00)
		embed.add_field(name="-mute", value="Mute a member so they cannot type or speak.", inline=False)
		embed.add_field(name="-ban", value="Ban a member.", inline=False)
		embed.add_field(name="-kick", value="Kick a member", inline=False)
		embed.add_field(name="-purge", value="Delete a number of messages from a channel", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)	
		
	if message.content.startswith('-help math'): 
		embed = discord.Embed(title=':scroll: __Math__',description='', color=0xFF8C00)
		embed.add_field(name="-add", value="Adds the two entered numbers. ", inline=False)
		embed.add_field(name="-sub", value="Subtracts the two entered numbers.", inline=False)
		embed.add_field(name="-multi", value="Multiplies the two entered numbers.", inline=False)
		embed.add_field(name="-div", value="Divides the two entered numbers.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)		
		
	if message.content.startswith('macrohelp fun'): 
		embed = discord.Embed(title=':scroll: __Fun__',description='', color=0xFF8C00)
		embed.add_field(name="-choose", value="Chooses one option from the list.", inline=False)
		embed.add_field(name="-meme", value="Displays a random meme.", inline=False)
		embed.add_field(name="-kill", value="Kills the mentioned user.", inline=False)
		embed.set_thumbnail(url='http://pngimg.com/uploads/question_mark/question_mark_PNG130.png')
		await client.send_message(message.channel, embed=embed)	
		
		
	if message.content.startswith('-announce'):
		if message.content[9:] =="":
			await client.send_message(message.channel, 'Error. Type in an announcement.')
		else:
			await client.send_message(message.channel, '{0.author.mention} Your announcement has been sent succesfully!'.format(message))
			args = message.content.split(" ")		
			channel=client.get_channel('568135270210207755')
			
			embed = discord.Embed(title='', color=0x3391D0)
			embed.add_field(name="__Announcement__", value= "```%s```" % (" ".join(args[1:])), inline=False)
			embed.add_field(name="By:", value="{0.message.author}".format(message), inline=False)
			embed.set_thumbnail(url="https://media.discordapp.net/attachments/566631626545823786/568131998523064320/ef94710266f57ca3e88c8cbe05fc4a8a.png?width=192&height=192")
			a=await client.send_message(channel, embed=embed)
			await client.add_reaction(a, "👍")
			await client.add_reaction(a, "👎")
			
	if message.content.startswith('-everyoneannounce'):
		if message.content[9:] =="":
			await client.send_message(message.channel, 'Error. Type in an announcement.')
		else:
			await client.send_message(message.channel, '{0.author.mention} Your announcement has been sent succesfully!'.format(message))
			args = message.content.split(" ")		
			channel=client.get_channel('568135270210207755')
			await client.send_message(channel, "@everyone")
			embed = discord.Embed(title='', color=0x3391D0)
			embed.add_field(name="__Announcement__", value= "```%s```" % (" ".join(args[1:])), inline=False)
			embed.add_field(name="By:", value="{0.message.author}".format(message), inline=False)
			embed.set_thumbnail(url="https://media.discordapp.net/attachments/566631626545823786/568131998523064320/ef94710266f57ca3e88c8cbe05fc4a8a.png?width=192&height=192")
			a=await client.send_message(channel, embed=embed)
			await client.add_reaction(a, "👍")
			await client.add_reaction(a, "👎")
			
			
	if message.content.upper().startswith('-KILL'):
		a=message.content[6:]
		if a == "":
			await client.send_message(message.channel, "<:alphaError:468832634542227477> Error. Mention someone to kill him.")
		else:
			list = ["{0.author.mention}".format(message) + " rips out " + a + "'s head and starts devouring on his brain cells." , "{0.author.mention}".format(message) + " decided to go to a dance party where his rival " + a + " was at. Later on, " + a +" said: 'I fucking hate this party' and " + "{0.author.mention}".format(message) + " shot him down in plain sight." , "{0.author.mention}".format(message) + " sent " + a+ "to the Sahara desert where " + a + " slowly starved to death." , "{0.author.mention}".format(message) + " found The Hammer of Thor, which explains why " +a+" became toast." , "{0.author.mention}".format(message) + " found a cancer pill, which explains how "+a+ " got cancer." , "{0.author.mention}".format(message) + " had prayed many nights to Poseidon to kill his/her mortal enemy, but he/she never thought he would send a ravenous sharknado to eat "+a+ " and their family! (and a few neighbors too)" , "{0.author.mention}".format(message) + " drowned "+a+ " in a freezing bathtub." , "{0.author.mention}".format(message) + " ordered his pet to attack " + a, "{0.author.mention}".format(message) +" Found a wand and casted 'EXPLODE' spell on " + a, "{0.author.mention}".format(message) + " pushed "+a+" into an active volcano. " , "{0.author.mention}".format(message) + " blindfolded " +a+" and took him/her to gym to kill him/her with a shotgun! " , "{0.author.mention}".format(message) +" has a particular proclivity for pyrotechnics and puts it to good use by strapping " +a+ " to a large rocket and sending him/her straight to the moon. " , "{0.author.mention}".format(message) +" shot " +a+ " with a *lazer gun*, but killed himself/herself due to the backfire." , "{0.author.mention}".format(message)+" threw "+a+" off a bridge." , "{0.author.mention}".format(message)+" helped "+ a +" fix a broken paintball gun, just to kill " + a + " with it."] 
			secure_random = random.SystemRandom()
			m=secure_random.choice(list)		
			await client.send_message(message.channel, m)




	if message.content.startswith('-help ping'):
		embed = discord.Embed(title="Command: -ping",description='**Description:** Pings the bot \n **Cooldown:** 3 seconds \n **Usage:** -ping', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help time'):
		embed = discord.Embed(title="Command: -time",description='**Description:** Current time in UK \n **Cooldown:** 5 seconds \n **Usage:** -time', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help add'):
		embed = discord.Embed(title="Command: -add",description='**Description:** Adds the two entered numbers \n **Cooldown:** 3 seconds \n **Usage:** -add \n **Example:** -add 10 5', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help sub'):
		embed = discord.Embed(title="Command: -sub",description='**Description:** Subtracts the two entered numbers \n **Cooldown:** 3 seconds \n **Usage:** -sub \n **Example:** -sub 10 5', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help multi'):
		embed = discord.Embed(title="Command: -multi",description='**Description:** Multiplies the two entered numbers \n **Cooldown:** 3 seconds \n **Usage:** -multi \n **Example:** -multi 10 5', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help div'):
		embed = discord.Embed(title="Command: -div",description='**Description:** Divides the two entered numbers \n **Cooldown:** 3 seconds \n **Usage:** -div \n **Example:** -div 10 5', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help choose'):
		embed = discord.Embed(title="Command: -choose",description='**Description:** Chooses one option from the list \n **Cooldown:** 3 seconds \n **Usage:** -choose \n **Example** -choose 1/2/3', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help rps'):
		embed = discord.Embed(title="Command: -rps",description='**Description:** To play rock/paper/scissors with the bot \n **Cooldown:** No cooldown \n **Usage:** -rps \n **Example:** -rps rock', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help flip'):
		embed = discord.Embed(title="Command: -flip",description='**Description:** To flip a coin \n **Cooldown:** No cooldown \n **Usage:** -flip \n **Example:** -flip heads', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help meme'):
		embed = discord.Embed(title="Command: -meme",description='**Description:** Displays a random meme \n **Cooldown:** 5 seconds \n **Usage:** -meme', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help kill'):
		embed = discord.Embed(title="Command: -kill",description='**Description:** Kills the mentioned user \n **Cooldown:** No cooldown \n **Usage:** -kill \n **Example:** -kill @Trocir', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help 8ball'):
		embed = discord.Embed(title="Command: -8ball",description='**Description:** Answers your yes/no questions \n **Cooldown:** No cooldown \n **Usage:** -8ball \n **Example:** -8ball [Question]', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help avatar'):
		embed = discord.Embed(title="Command: -avatar",description='**Description:** Displays the avatar of the mentioned user \n **Cooldown:** 3 seconds \n **Usage:** -avatar \n **Example:** -avatar @Trocir', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help userinfo'):
		embed = discord.Embed(title="Command: -userinfo",description='**Description:** Displays the mentioned users info \n **Cooldown:** 3 seconds \n **Usage:** -userinfo \n **Example:** -userinfo @Trocir', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help serverinfo'):
		embed = discord.Embed(title="Command: -serverinfo",description='**Description:** Displays the server stats  \n **Cooldown:** 3 seconds \n **Usage:** -serverinfo', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('-help credits'):
		embed = discord.Embed(title="Command: -credits",description='**Description:** Displays the bots info \n **Cooldown:** 5 seconds \n **Usage:** -credits', color= 0x546E7A)
		await client.send_message(message.channel, embed=embed)

  
client.run(str(os.environ.get('BOT_TOKEN')))
