import discord
from discord import channel

token = open("token.txt", "r").read()
client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message : discord.Message):

    if message.author==client.user :
        print(f"Self message")
    
    if message.content=="Commands.member_count" :
        print("Memeber count called")
        await message.channel.send(f"There are {message.guild.member_count} members in your server")

client.run(token)