import discord
from discord.ext import commands

intents = discord.Intents.all()
token = open("token.txt", "r").read()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.listen()
async def on_ready() :
    print("Bot ready for deployment")


@bot.listen()
async def on_guild_join(message: discord.Message) :
    print(f"Joined server {message.guild.name}")
    await message.channel.send("Hello!")


@bot.command(name="mcount")
async def member_count(ctx : commands.Context):
    await ctx.send(f"Member count : {ctx.message.guild.member_count}")


@bot.command(name="mstats")
async def member_stats(ctx : commands.Context):
    online = 0
    offline = 0
    idle = 0

    members = ctx.message.guild.members
    for m in members :
        if str(m.status) == "online":
            online += 1
        elif str(m.status) == "offline":
            offline += 1
        else:
            idle += 1

    await ctx.send(
        f"```Members \t\t: {len(members)}\nOnline members  : {online}\nOffline members : {offline}\nIdle/Hidden \t: {idle}```")

bot.run(token)