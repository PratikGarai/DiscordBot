import discord
from discord.ext import commands

from SarcasmModel import SarcasmModel as SarcasmModule

intents = discord.Intents.all()
token = open("token.txt", "r").read()
bot = commands.Bot(command_prefix='!', intents=intents)

modules = {
    "sarcasm" : True
}


@bot.listen()
async def on_ready() :
    print("Bot ready for deployment")


@bot.listen()
async def on_message(message : discord.Message) :
    if message.author==bot.user :
        return 
    
    try : 
        if not message.content[0].isalpha() :
            return 
    
        if modules["sarcasm"] :
            res = sarcasm.get_sarcasm(message.content)
            if res["result"] : 
                await message.add_reaction("😎")
            else :
                await message.add_reaction("😐")
    except : 
        pass


@bot.listen()
async def on_guild_join(guild) :
    print(f"Joined server {guild.name}")


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


sarcasm = SarcasmModule()
bot.run(token)