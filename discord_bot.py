import discord
from discord.ext import commands
from discord.ext.audiorec import NativeVoiceClient
import asyncio
import random
import io
import wavelink


intents = discord.Intents.all()
client = commands.Bot(command_prefix="pls ", intents=intents)



#initiation#
@client.event
async def on_ready():
    print("READY!")
    asyncio.create_task(change_status())

#change statuses#
async def change_status():
    status = ["ayaka is the best", "28 days left"] #"ayaka is the best","ayaka #1"
    index = 0
    while True:
        status_chose = status[index]
        await client.change_presence(activity=discord.Game(name=status_chose))
        index += 1
        if index == len(status):
            index = 0
        await asyncio.sleep(60)     


#delete messages#
@client.command(aliases = ['clean','del','delete'])
async def clear(ctx,amount=1):
    print(ctx.author,client.user)
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(content = f"{amount} messages deleted.", delete_after = 2)
    

#!csgo#
@client.command()
async def csgo(ctx):
    with open("csgo.txt","r") as file:
        data = file.read()
        print(data)
        await ctx.send(data)

#pls choose#
@client.command()
async def choose(ctx,*arg):
    await ctx.send(f'{arg[random.randint(0,len(arg)-1)]}')

#countdown#
@client.command()
async def countdown(ctx,second):
    minute = 0
    second = int(second)
    if second < 0:
        await ctx.send("no negative numbers la")
    else:
        while second > 60:
            second -= 60
            minute += 1
        message = await ctx.send(f"time remaining: {minute} minute {second} second")
        while second > -1 or minute != 0 :
            await message.edit(content = f"time remaining: {minute} minute {second} second")    
            await asyncio.sleep(1)
            second -= 1
            if minute != 0 and second == 0:
                minute -= 1
                second += 60
        else:
            await ctx.send("Done!")



#join channel#
@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        global channel
        channel = ctx.message.author.voice.channel
        await channel.connect(cls = NativeVoiceClient)


    else:
        await ctx.send(content = "Not In Channel",delete_after = 2)

#record audio#
@client.command()
async def record(ctx):
    second = 0
    minute = 0
    global sw
    sw = True
    ctx.voice_client.record(lambda e: print(f"Exception: {e}"))
    message = await ctx.send(f"Recording Started **[ Time Elapsed: {second} second ]**")
    while sw:
        await asyncio.sleep(1)
        second += 1
        if second == 60:
            second = 0
            minute += 1
        if minute != 0:
            await message.edit(content = f"Recording Started **[ Time Elapsed: {minute} minute {second} second ]**")
        else:
            await message.edit(content = f"Recording Started **[ Time Elapsed: {second} second ]**")

#stop recording#
@client.command()
async def stop(ctx):

    try:
        if ctx.voice_client.is_recording() == True:
            global sw
            sw = False
            second = 5
            message = await ctx.send("Waiting for **5** second(s)")
            for i in range(5):
                await asyncio.sleep(1)
                second -= 1
                await message.edit(content = f"Waiting for **{second}** second(s)")
            wav_bytes = await ctx.voice_client.stop_record()
            wav_file = discord.File(io.BytesIO(wav_bytes), filename="Recorded.wav")
            await ctx.send(file = wav_file)
    except:
        await ctx.send("Not Recording")

#play song# ##java -jar Lavalink.jar
@client.command()
async def play(ctx):
    await client.wait_until_ready()
    node = await wavelink.NodePool.create_node(bot=client,
                                              host = '127.0.0.1',
                                              port = 2333,
                                              password = 'youshallnotpass')

    
#disconnect#
@client.command(aliases = ["disconnect","disc","quit"], pass_context = True)
async def leave(ctx):
    try:
        await ctx.message.guild.voice_client.disconnect()
    except:
        await ctx.send("?")



client.run('x')

