import discord
from discord.ext import commands

class PollModule :
    def __init__(self) :
        pass

    async def analyseMessage(self, ctx : commands.Context, id : int) :
        msg : discord.Message = await ctx.fetch_message(id)
        reactions = msg.reactions

        resp = "<table><thead>"
        users = set({})
        for reaction in reactions :
            resp += f"<th>{reaction.emoji}</th>"
            usrs = await reaction.users().flatten()
            for i in usrs : 
                if i not in users :
                    users.add(i)
        
        resp+="</thead><tbody>"
        tick = "✔️"

        table = { user : ["" for i in reactions] for user in users }
        for ind, reaction in enumerate(reactions) : 
            usrs = await reaction.users().flatten()
            for user in usrs :
                table[user][ind] = tick
        
        for user, reaction in table.items() :
            resp += f"<tr><td>{user.display_name}</td>"
            for r in reaction :
                resp += f"<td>{r}</td>"
            resp += "</tr>"
        
        resp += "</tbody></table>"

        # await ctx.send(f"```html{resp}```")
        print(resp)