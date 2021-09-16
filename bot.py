import discord
from discord.ext import commands

intents = discord.Intents.all()
token = open("token.txt", "r").read()
bot = commands.Bot(command_prefix='!', intents=intents)


from SarcasmModel import SarcasmModel as SarcasmModule
from StatsModule import memberCounter, memberStatistics

modules = {
    "sarcasm" : SarcasmModule(),
    "stats" : True
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
            res = modules["sarcasm"].get_sarcasm(message.content)
            if res["result"] : 
                await message.add_reaction("😎")
            else :
                await message.add_reaction("😐")
    except : 
        pass


@bot.command(name="toggle")
async def member_count(ctx : commands.Context, module : str):
    print(ctx.author.id)


@bot.command(name="mcount")
async def member_count(ctx : commands.Context):
    if modules["stats"] :
        count = await memberCounter(ctx)
        await ctx.send(f"Member count : {count}")
    else :
        await ctx.send("```Command is blocked for now```")


@bot.command(name="mstats")
async def member_stats(ctx : commands.Context):
    if modules["stats"] :
        online, offline, idle, members = await memberStatistics(ctx)
        await ctx.send(
            f"```Members \t\t: {len(members)}\nOnline members  : {online}\nOffline members : {offline}\nIdle/Hidden \t: {idle}```")
    else :
        await ctx.send("```Command is blocked for now```")

bot.run(token)