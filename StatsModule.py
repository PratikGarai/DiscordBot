from discord.ext import commands

class StatsModule :

    def __init__(self) :
        pass


    async def memberCounter(self, ctx : commands.Context):
        return ctx.message.guild.member_count


    async def memberStatistics(self, ctx : commands.Context):
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