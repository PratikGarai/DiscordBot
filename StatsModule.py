from discord.ext import commands

async def memberCounter(ctx : commands.Context):
    return ctx.message.guild.member_count


async def memberStatistics(ctx : commands.Context):
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

    return online, offline, idle, members