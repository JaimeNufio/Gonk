import discord
import re
import json
from datetime import datetime
from discord import message

import youtube_dl
import asyncio
import time

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

async def SummonVoice(ctx,bot,which,var=1): #which is a string
    if not ctx.author.voice:
        print("Step 1 Fail: trigger isn't in a voice channel")
        #await ctx.send("{} is not connected to a voice channel".format(ctx.author.name))
        return

    channel = ctx.author.voice.channel
        #await channel.connect()

    task = asyncio.create_task(channel.connect())
    done, pending = await asyncio.wait({task})

    if task in done:
        
        if which == "ahh":
            print("AHHH TRIGGER")
            await AHHH(ctx,bot)
        if which == "yubi":
            await YUBIYUBI(ctx,bot)
        if which == "waterinthefire":
            await WaterInTheFire(ctx,bot)
        if which == 'wow':
            await Wow(ctx,bot,var)
        if which == 'cum':
            await Cum(ctx,bot,var)

async def AHHH(ctx,bot):

    server = ctx.guild
    voice_channel = server.voice_client
    try:
        #For Windows, we just put ffmpeg exe in this same folder, lol
        #voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="ahhh.m4a"))

        if voice_channel: 
            voice_channel.play(discord.FFmpegPCMAudio(source="./assets/sounds/ahhh.mp3")) 

    except Exception as e:
        print(e)
        await ctx.send(e)
    finally:
        if voice_channel:
            time.sleep(4)
            await leave(ctx,bot)   

async def leave(ctx,bot):
    voice_client = ctx.guild.voice_client

    if not voice_client:
        await ctx.send("AHHHH?")

    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

async def Wow(ctx,bot,var):

    server = ctx.guild
    voice_channel = server.voice_client
    try:
        #For Windows, we just put ffmpeg exe in this same folder, lol
        #voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="ahhh.m4a")) 
        voice_channel.play(discord.FFmpegPCMAudio(source="./assets/sounds/wow.mp3")) 
    except Exception as e:
        print(e)
    finally:
        scale = 5 # how much to divide run time by (1 = string length)
        base = 1
        time.sleep(((15-base) if var/scale > (15-base) else var/scale)+base)
        await leave(ctx,bot)  

async def Cum(ctx,bot,var):

    server = ctx.guild
    voice_channel = server.voice_client
    try:
        #For Windows, we just put ffmpeg exe in this same folder, lol
        #voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="ahhh.m4a")) 
        voice_channel.play(discord.FFmpegPCMAudio(source="./assets/sounds/cyberpunk_sound.mp3")) 
    except Exception as e:
        print(e)
    finally:
        time.sleep(4)
        await leave(ctx,bot)  

async def YUBIYUBI(ctx,bot):

    server = ctx.guild
    voice_channel = server.voice_client
    try:
        #For Windows, we just put ffmpeg exe in this same folder, lol
        #voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="ahhh.m4a")) 
        voice_channel.play(discord.FFmpegPCMAudio(source="./assets/sounds/yubiyubi.mp3")) 
    except Exception as e:
        print(e)
    finally:
        time.sleep(3)
        await leave(ctx,bot)   

async def WaterInTheFire(ctx,bot):

    server = ctx.guild
    voice_channel = server.voice_client
    try:
        #For Windows, we just put ffmpeg exe in this same folder, lol
        #voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="ahhh.m4a")) 
        voice_channel.play(discord.FFmpegPCMAudio(source="./assets/sounds/waterinthefire.mp3")) 
    except Exception as e:
        print(e)
    finally:
        time.sleep(3.75)
        await leave(ctx,bot)  

# async def leave(ctx,bot):
#     voice_client = ctx.guild.voice_client
#     if voice_client.is_connected():

#         await voice_client.disconnect()
#     else:
#         await ctx.send("The bot is not connected to a voice channel.")
