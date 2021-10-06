from discord.ext import commands

class StatsModule :

    def __init__(self) :
        pass


    async def memberCounter(self, ctx : commands.Context):
        count = ctx.message.guild.member_count
        await ctx.send(f"```Member count in this server : {count}```")


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

        await ctx.send(
            f"```Members \t\t: {len(members)}\nOnline members  : {online}\nOffline members : {offline}\nIdle/Hidden \t: {idle}```")
    

    async def memberCounterHere(self, ctx : commands.Context):
        count = len(ctx.message.channel.members)
        await ctx.send(f"```Member count in this channel : {count}```")


    async def memberStatisticsHere(self, ctx : commands.Context):
        online = 0
        offline = 0
        idle = 0

        members = ctx.message.channel.members
        for m in members :
            if str(m.status) == "online":
                online += 1
            elif str(m.status) == "offline":
                offline += 1
            else:
                idle += 1

        await ctx.send(
            f"```Members \t\t: {len(members)}\nOnline members  : {online}\nOffline members : {offline}\nIdle/Hidden \t: {idle}```")
