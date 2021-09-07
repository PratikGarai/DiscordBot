import discord
import logging

logging.basicConfig()
logger = logging.getLogger("my-logger")
logger.setLevel(logging.INFO)

token = open("token.txt", "r").read()
client = discord.Client()

@client.event
async def on_ready():
    logger.info(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    logger.info(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if "hello" in message.content.lower():
        await message.channel.send("Hi!")

client.run(token)