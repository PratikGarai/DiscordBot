from discord.ext import commands


async def checkModuleBlocked(ctx : commands.Context, modules_dict, module) :
    if modules_dict[module] :
        return True
    
    else :
        await ctx.send(f'```Command is blocked for now. Activate "{module}" module to use this command.```')
        return False