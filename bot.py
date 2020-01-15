import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = '.', case_insensitive = True)

@client.event
async def on_ready():
    print('Bot is ready')
    return await client.change_presence(activity = discord.Activity(type = 1, name = 'Tutorial', url = 'https://twitch.tv/xQcOW'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.command()
async def ping(ctx):
    await ctx.send('pong')

client.run('NjY2Njk1MzU4ODIyNDgxOTQw.Xh5zrQ.QkefaAEQknuzz7nwdhXoy8K1l6A')
