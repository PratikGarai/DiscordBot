import discord
from discord.ext import commands

class PollModule :
    def __init__(self) :
        pass

    async def analyseMessage(self, ctx : commands.Context, id : int) :
        tick = "✔️"

        msg : discord.Message = await ctx.fetch_message(id)
        reactions = msg.reactions

        emjs = []
        mxl = 0
        users = set({})
        for reaction in reactions :
            emjs.append(reaction.emoji)
            usrs = await reaction.users().flatten()
            for i in usrs : 
                if i not in users :
                    users.add(i)
                    mxl = max(mxl, len(i.display_name))

        table = { user : ["" for i in reactions] for user in users }
        for ind, reaction in enumerate(reactions) : 
            usrs = await reaction.users().flatten()
            for user in usrs :
                table[user][ind] = tick
        
        mxl += 4
        head = "+"+"="*mxl
        row1 = f'|{str.center("Name", mxl)}|'
        for emj in emjs : 
            head += "+"+"="*5
            row1 += f'{str.center(emj, 4)}|'
        head += "+"

        t = f"{head}\n{row1}\n{head}\n"
        
        for user, reaction in table.items() :
            row = f'|{str.center(user.display_name, mxl)}|'
            for r in reaction :
                row += f'{str.center("x" if r!="" else " ", 5)}|'
            t += row+"\n"
        
        t += head

        await ctx.send(f"```{t}```")
