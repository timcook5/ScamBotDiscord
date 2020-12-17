import discord
from discord.ext import commands
import random
import time
import re
import datetime

class scamcmd:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def number(self, ctx):
		Scamlist = open('Scamlist.lst', 'r')
		Numbers = Scamlist.read().splitlines()
		random.seed()
		RandNum = Numbers[random.randint(0,len(Numbers)-1)]
		await self.bot.say(':mailbox_with_mail: {} **Check your DM**'.format(ctx.message.author.mention))
		author = ctx.message.author
		try:
			await self.bot.send_message(author, '**Here is your number** ``{}``'.format(RandNum))
		except Exception as e:
			await self.bot.say('OOF I can\'t seem to DM you, sorry!')

	@commands.command(pass_context=True)
	async def submit(self, ctx):
		await self.bot.delete_message(ctx.message)
		if ctx.message.server == None:
			await self.bot.say('Sorry, please do these in DMs (It\'s to protect scambaiting servers)')
			return
		number = ctx.message.content[8:]
		if len(number) == 0:
			await self.bot.say('No number submitted. Please add a number')
			return
		if len(number) == 14:
			pattern = re.compile('18[0-8]{2}-[0-9]{3}-[0-9]{4}')
			if re.match(pattern,number) == None:
				await self.bot.say('Sorry, that number does not match our filter, if this is a scam number, please dm <@341928732602269698> to improve the filter.')
				return
		if len(number) == 13:
			pattern = re.compile('8[0-8]{2}-[0-9]{3}-[0-9]{4}')
			if re.match(pattern,number) == None:
				await self.bot.say('Sorry, that number does not match our filter, if this is a scam number, please dm <@341928732602269698> to improve the filter.')
				return
		if len(number) == 11:
			pattern = re.compile('18[0-8]{2}[0-9]{3}[0-9]{4}')
			if re.match(pattern,number) == None:
				await self.bot.say('Sorry, that number does not match our filter, if this is a scam number, please dm <@341928732602269698> to improve the filter.')
				return
		if len(number) == 10:
			pattern = re.compile('8[0-8]{2}[0-9]{7}')
			if re.match(pattern,number) == None:
				await self.bot.say('Sorry, that number does not match our filter, if this is a scam number, please dm <@341928732602269698> to improve the filter.')
				return
		else:
			await self.bot.say("Hmmm, not the right length, sorry.")
			return
		print("Opening List")
		currentList = open('Scamlist.lst', 'r')
		print("Reading list")
		list = currentList.read().splitlines()
		if number in list:
			print('In DB')
			await self.bot.say('This number is already in our database, but thank you for contributing!')
			currentList.close()
			return
		currentList.close()
		print("Opening list in append mode")
		Scam = open('Scamlist.lst', 'a')
		print("Writing to list")
		Scam.write(number+'\n')
		await self.bot.say('Number written.')
		Scam.close()


	@commands.command(pass_context=True)
	async def report(self, ctx):
		return

def setup(bot):
	bot.add_cog(scamcmd(bot))
