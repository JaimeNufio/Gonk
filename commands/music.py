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

async def AHH(ctx,bot):
    if not ctx.author.voice:
        print("Step 1 Fail: trigger isn't in a voice channel")
        #await ctx.send("{} is not connected to a voice channel".format(ctx.author.name))
        return

    channel = ctx.author.voice.channel
        #await channel.connect()

    task = asyncio.create_task(channel.connect())
    done, pending = await asyncio.wait({task})

    if task in done:
        await AHHH(ctx,bot)

async def AHHH(ctx,bot):

    server = ctx.guild
    voice_channel = server.voice_client
    try:
        #filename = await YTDLSource.from_url("https://www.youtube.com/watch?v=gK6B7wweIWs", loop=bot.loop)
        voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="ahhh.m4a")) 
    except Exception as e:
        print(e)
    finally:
        time.sleep(3)
        await leave(ctx,bot)

        

async def leave(ctx,bot):
    voice_client = ctx.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

