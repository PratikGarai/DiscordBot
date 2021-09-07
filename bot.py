import discord
from discord.ext import commands

token = open("token.txt", "r").read()
bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(token)