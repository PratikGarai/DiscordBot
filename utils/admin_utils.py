from discord.ext import commands

def get_admins() :
    admins = []
    admins.append(int(open("admin_id.txt", "r").read()))

    return admins


def isAdmin(id : int) :
    return id in get_admins()


async def adminVerifyAndReact(ctx : commands.Context) :
    if isAdmin(ctx.author.id) :
        await ctx.message.add_reaction("🙇")
        return True 
    else :
        await ctx.message.add_reaction("⛔")
        await ctx.send(f"```Sorry, you do not have such authority. 👮```")
        return False