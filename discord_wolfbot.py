import discord
import asyncio
import logging
import random
from discord.ext.commands import Bot

Client = Bot(command_prefix='!')

@Client.event
async def on_ready():
	print('Logged in as')
	print(Client.user.name)
	print(Client.user.id)
	print('-----------------------')

#Add message to delete on prompt
to_delete_messages = [";;play", ";;stop", ";;skip", ";;restart", ";;replay"]

@Client.event	
async def on_message(message):
	if message.content.startswith("$hello"):
		await Client.send_message(message.channel, 'Hi, {}!'.format(message.author))

	if message.content.partition(' ')[0].lower() in to_delete_messages:
		await asyncio.sleep(1)
		await Client.delete_message(message)

	if message.content.startswith("$list"):
		await Client.send_message(message.channel, "Words to delete on prompt: {}".format(to_delete_messages))

	await Client.process_commands(message)

@Client.command(pass_context=True)	
async def clear(ctx, number: int):
	mgs=[]	
	tmp= await Client.say("Working!!!")
	async for x in Client.logs_from(ctx.message.channel, limit=number):
		mgs.append(x)
	await Client.delete_messages(mgs)	
		

@Client.command(pass_context=True)
async def purge(ctx, number: int):
	tmp= await Client.say("Starting purge...")
	async for x in Client.logs_from(ctx.message.channel, limit=number):
		if x:
 			await Client.delete_message(x)

@Client.command() 
async def rolldice(number : int):	
	result = str(random.randint(1, number))
	await Client.say("Random number: " + result)

@Client.command()
async def roll(number=2):
	result = str(random.randint(1, number))
	await Client.say("Random number: " + result)

@Client.command(pass_context=True)
async def add_list(ctx, word : str):

	member = ctx.message.author	
	channel = ctx.message.channel

	if member.permissions_in(channel).administrator:
		if word.lower() not in to_delete_messages:
			to_delete_messages.append(word.lower())
			tmp = await Client.say("{} has been added to the list".format(word))
		else: 
			await Client.say("{} is already in list".format(word))	

@Client.command (pass_context=True)
async def del_list(ctx, word : str):

	member = ctx.message.author
	channel = ctx.message.channel

	if member.permissions_in(channel).administrator:

		if word.lower() in to_delete_messages:
			to_delete_messages.remove(word)
			tmp = await Client.say("{} has been deleted from the list.".format(word))

		else:
			await Client.say("Word not in list.")

""""@Client.event
async def on_error(event):
	r = '!clear + #mgs\n!purge + #mgs'
	await Client.send_message(message.channel,'Command not found.\nCommands: {}'.format(r))"""

	
 		
Client.run("MzE5Mjc3OTczNTQwNzAwMTcx.DA-niw.pWRWqQalc_oaq5AqkmbfJRLqNuo")
