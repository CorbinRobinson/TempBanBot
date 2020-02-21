import discord
from discord.ext import commands
import random
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    return await client.change_presence(activity = discord.Activity(type = 1, name = 'the fall of the bourgeoisie', url = 'https://twitch.tv/xQcOW'))

async def is_me(ctx):
    return ctx.author.id == 191617352083832832

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # 191617352083832832 my id
    # 202504795582365697 bo id
    # 679444918757752883 scooby id
    # 666838418134925347 lab channel id
    if message.author.id == 202504795582365697:
        bWords = [
            "Scubarooni",
            "scubarooni",
            "Scuba",
            "scuba",
            "Corbin",
            "corbin"
        ]
        mentionedMe = False
        for user in message.mentions:
            if user.id == 191617352083832832:
                mentionedMe = True

        if message.content in bWords or mentionedMe:
            response = [
                "Silence, prisoner.",
                "Keep it down, hoodlum.",
                "ಠ_ಠ",
                "You have no rights, scum.",
                "Time to get the gag ( ͡° ͜ʖ ͡°)"
            ]
            await message.delete(delay=0.0)
            await message.channel.send(random.choice(response))
            await message.channel.send(f'Banned {message.author.mention}')
            await message.author.ban(reason = "Bein a dumb bitch")


    await client.process_commands(message)

@client.event
async def on_member_join(member):
    if member.id == 202504795582365697:
        for c in member.guild.channels:
            await c.set_permissions(member, send_tts_messages = False, embed_links = False, attach_files = False, mention_everyone = False)
            if c.id == 633369722557300774:
                await c.set_permissions(member, embed_links = True, attach_files = True)

@client.command()
async def list(ctx):
     cmds = [
         "  GENERAL COMMANDS \n",
         "-------------------- \n",
         "8ball - ask a question, get an answer \n",
         "ping - pongn \n",
         "   ADMIN COMMANDS \n",
         "-------------------- \n",
         "stop - turns bot off \n",
         "unban - unbans user#number \n"
     ]
     await ctx.channel.send(cmds)
     return

@client.command()
@commands.check(is_me)
async def unban(ctx, *, member):
    banned = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for entry in banned:
        user = entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.send(f'Unbanned {user.mention}')
            return

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
    await ctx.send(f'Answer: {random.choice(responses)}')

@client.command()
@commands.check(is_me)
async def stop(ctx):
    await client.close()

client.run('NjY2Njk1MzU4ODIyNDgxOTQw.Xj5nyg.elZ1_pvj1fXgGwghUUQsleioD7w')
