from logging import exception
import discord
from discord import message
from discord.ext.commands import context
import commands.basekit as shell 
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import json
import codecs

from commands import utils
from commands import quotes as quotesModule
from commands import rename as renameModule
from commands import music as musicModule
from extras import conditions as extras
from records import firestore
from extras import sus
from extras import reminder
from extras import tts

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(client,sync_commands=True)

guild_ids = []
token = ""

with open("credentials.json","r") as file:
    creds = json.load(file)
    token = creds['token']
    guild_ids = creds['guild_ids']

@client.event
async def on_ready():
    firestore.init('firebase.json')
    print('Logged on as {0}!'.format(client.user))

    with codecs.open('nicknames.txt','w','utf-8') as f:

        first = True
        for item in firestore.GetNicknameHistoryStream():
            
            curr = item.to_dict()
            try:
                if (not curr['renamer'] or not curr['user'] or not curr['nickname']
                    or not curr['serverid'] or not curr['when'] ):
                    print("Skipping:")
                    print(curr)
                    continue
            except:
                print(curr)
                continue
            

            vals = item.to_dict().values()
            if first:
                selected=['serverid','nickname','user','renamer','when']
                f.write("@@@".join([str(i) for i in selected])+"\n")
                first = False

            row = [str(i) for i in [item.to_dict()['serverid'],
                item.to_dict()['nickname'],
                item.to_dict()['user'],
                item.to_dict()['renamer'],
                item.to_dict()['when'],
            ]]

            line = "@@@".join([str(i) for i in row]) 
            f.write(line+"\n")

        
    with codecs.open('usermap.txt','w','utf-8') as f:
        for guild in client.guilds:
            async for member in guild.fetch_members():
                # print(member.name,":",member.id)
                f.write("@@@".join([str(i) for i in [member.id,member.name,guild.name,"\n"]]))

client.run(token)
