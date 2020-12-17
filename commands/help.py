import discord
from discord.ext import commands

class help:

    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    @commands.command(pass_context=True, name="help", aliases=["Help", "HELP", "cmd", "Cmd", "CMD", "cmds", "Cmds", "CMDS", "commands", "Commands", "COMMANDS"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def help(self, ctx):
        author = ctx.message.author
        help=discord.Embed(colour=discord.Colour(value=0xFFDFF0))
        help.add_field(name="Submit", value="Allows you to submit a number", inline=True)
        help.add_field(name="Number", value="Gives you a random number from the list", inline=True)
        help.add_field(name="Report", value="Reports a number as not working", inline=True)
        #help.add_field(name="", value="", inline=True)
        await self.bot.say(embed=help)

def setup(bot):
    bot.add_cog(help(bot))
