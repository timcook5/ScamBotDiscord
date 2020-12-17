import asyncio
import discord
from discord.ext import commands
import random
import time
import re
import datetime
import botkey
from os import listdir
from os.path import isfile, join
import sys, traceback

description = '''This bot is built to serve as a number bot that will be able to manage numbers for scambaiting communities'''
bot = commands.Bot(command_prefix='=', description=description)
client = discord.Client()

cmd_dir = "commands"

if __name__ == "__main__":
	for extension in [f.replace('.py', '') for f in listdir(cmd_dir) if isfile(join(cmd_dir, f))]:
		try:
			bot.load_extension(cmd_dir + "." + extension)
		except Exception as e:
			print('Failed to load extension {extension}')
			traceback.print_exc()

@bot.command(pass_context=True)
async def invite(ctx):
	id = bot.id
	await self.bot.say("**Invite me here :smirk:\nhttps://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=388161**".format(id))

@bot.event
async def on_command_error(error, ctx):
	author = ctx.message.author
	authorm = ctx.message.author.mention
	if isinstance(error, commands.CommandOnCooldown):
		response = await bot.send_message(ctx.message.channel, content="**:x: This command is on a %.2fs cooldown {}**".format(author) % error.retry_after)
		time.sleep(3)
		await bot.delete_message(response)
		return
	if isinstance(error, commands.CommandNotFound):
		response = await bot.send_message(ctx.message.channel, content="**:x: {} Command not found**".format(authorm))
		time.sleep(3)
		await bot.delete_message(response)
		return
	if isinstance(error, commands.MissingRequiredArgument):
		response = await bot.send_message(ctx.message.channel, content="**:x: {} Missing Arguments**".format(authorm))
		time.sleep(3)
		await bot.delete_message(response)
		return
	print(error)
	error=discord.Embed(description="**:x: Got an Error**\n```py\n{}\n```".format(error), colour=discord.Colour(value=0xff0707))
	error.add_field(name="User", value="{}".format(authorm), inline=True)
	error.add_field(name="Command+Content", value="{}".format(ctx.message.content), inline=True)
	await bot.send_message(ctx.message.channel, embed=error)
	return

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('-'*18)

@bot.event
async def on_message(message):
	if message.server is None and message.author != bot.user:
		print('Got DM from {} that says: {}'.format(message.author,message.content))
	await bot.process_commands(message)

bot.run(botkey.getToken())
