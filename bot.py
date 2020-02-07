import discord
from discord.ext import commands
import random
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')
    return await client.change_presence(activity = discord.Activity(type = 1, name = 'the fall of the bourgeoisie', url = 'https://twitch.tv/xQcOW'))

async def is_me(ctx):
    return ctx.author.id == 191617352083832832

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == 666838418134925347 and message.author.name == 'dodomino14':
        await message.channel.send('Silence, prisoner.')
        await message.delete(delay=0.0)

    await client.process_commands(message)


'''
@client.event
async def on_message(self, message):
    print('Message from {0.author}: {0.content}'.formate(message))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    await client.process_commands(message)
'''
@client.command()
async def ping(ctx):
    print('pong')
    await ctx.send(f'pong {round(client.latency * 1000)}ms')

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
@commands.check(is_me)
async def stop(ctx):
    await client.close()


'''
@client.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit = amount)
'''



client.run('NjY2Njk1MzU4ODIyNDgxOTQw.Xh6Suw.ouIfrcTDmrBuWY-L8LBEAUl_d1g')
