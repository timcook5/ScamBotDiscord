import discord
from discord.ext import commands

class admincmd:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        authorN = ctx.message.author
        id = authorN.id
        if int(id) == 341928732602269698:
            try:
                await self.bot.say('Alright! See ya!')
                await self.bot.close()
            except Exception as e:
                await self.bot.say('OOF ```{}```'.format(e))
                return
        else:
            await self.bot.say("No. You do not have permission to stop me {}.".format(ctx.message.author.mention))
            print("SOMEONE TRIED TO USE A FORBIDDEN COMMAND!!! {0.name} attempted to stop me in {0.server}!".format(ctx.message.author))
            return

def setup(bot):
    bot.add_cog(admincmd(bot))
