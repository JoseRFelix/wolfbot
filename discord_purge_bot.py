import discord
import asyncio
import logging
from discord.ext.commands import Bot

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

Client = Bot(command_prefix='!')

@Client.event
async def on_ready():
	print('Logged in as')
	print(Client.user.name)
	print(Client.user.id)
	print('-----------------------')

@Client.event
async def on_message(message):
	if message.content.startswith('!hello'):
		await Client.send_message(message.channel, 'Hello!!!')		
		
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
 		
Client.run('MzE2MDM5NDI1OTQ1NjMyNzY4.DAPeXA.Z-m2BZ_bbhF5Ezc0Nu5S_mcBYHk')