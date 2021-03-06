import discord
from discord.ext import commands

intents = discord.Intents.all()
token = open("token.txt", "r").read()
bot = commands.Bot(command_prefix='!', intents=intents)

from utils.admin_utils import adminVerifyAndReact
from utils.module_utils import checkModuleBlocked

from modules_states import states

modules = {
    # "sarcasm" : None,
    "stats" : None,
    "connect4" : None,
    "poll" : None
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
async def toggler(ctx : commands.Context, module : str):
    if await adminVerifyAndReact(ctx) :
        if module in modules : 
            if modules[module] :
                new_state = "off"
                modules[module] = None
            else :
                new_state = "on"
                modules[module] = states[module]
            await ctx.send(f"```Sure sir! 👍\nTurned {new_state} module : {module}```")
        else :
            await ctx.send(f"```Sorry sir, that module doesn't exist. 🙁```")

    
@bot.command(name="modAllOn")
async def allOn(ctx : commands.Context):
    if await adminVerifyAndReact(ctx) :
        for module in modules : 
            modules[module] = states[module]
        await ctx.send(f"```Sure sir! 👍\nTurned on all modules```")


@bot.command(name="modAllOff")
async def allOff(ctx : commands.Context):
    if await adminVerifyAndReact(ctx) :
        for module in modules : 
            modules[module] = None
        await ctx.send(f"```Sure sir! 👍\nTurned off all modules```")


@bot.command(name="modList")
async def modules_list(ctx : commands.Context):
    await ctx.message.add_reaction("👌")
    if len(modules.keys())!=0 :
        s = "```Here is the list of available modules :"
        for ind, i in enumerate(modules.keys()) :
            if modules[i] :
                s += f"\n\t{ind+1}.\t(ON)  {i}"
            else :
                s += f"\n\t{ind+1}.\t(OFF) {i}"
        s += "\n```"
        await ctx.send(s)
    else :
        await ctx.send("No modules found 🙁")


@bot.command(name="mcount")
async def member_count(ctx : commands.Context):
    if await checkModuleBlocked(ctx, modules, "stats"):
        await modules["stats"].memberCounter(ctx)


@bot.command(name="mstats")
async def member_stats(ctx : commands.Context):
    if await checkModuleBlocked(ctx, modules, "stats"):
        await modules["stats"].memberStatistics(ctx)


@bot.command(name="mcountHere")
async def member_countHere(ctx : commands.Context):
    if await checkModuleBlocked(ctx, modules, "stats"):
        await modules["stats"].memberCounterHere(ctx)


@bot.command(name="mstatsHere")
async def member_statsHere(ctx : commands.Context):
    if await checkModuleBlocked(ctx, modules, "stats"):
        await modules["stats"].memberStatisticsHere(ctx)


@bot.command(name="startc4")
async def connect4start(ctx : commands.Context, player1, player2) :
    if await checkModuleBlocked(ctx, modules, "connect4"):
        g = modules["connect4"]
        await g.start_game(ctx, player1, player2)


@bot.command(name="playc4")
async def connect4play(ctx : commands.Context, col) :
    if await checkModuleBlocked(ctx, modules, "connect4"):
        g = modules["connect4"]
        await g.play(ctx, col)


@bot.command(name="pollRead")
async def readPoll(ctx : commands.Context) :
    if await checkModuleBlocked(ctx, modules, "poll"):
        p = modules["poll"]
        await p.analyseMessage(ctx)


bot.run(token)