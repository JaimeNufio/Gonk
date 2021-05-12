from logging import exception
import discord
from discord import message
from discord.ext.commands import context
import commands.basekit as shell 
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
import json

from commands import utils
from commands import quotes as quotesModule
from commands import rename as renameModule

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(client,sync_commands=True)


#rename
@slash.slash(
    name="rename",
    description="Rename a nerd.",
    options=[
        create_option(
            name="target",
            description="User to nickname.",
            option_type=6,
            required=True
        ),
        create_option(
            name="nickname",
            description="Nickame for user.",
            option_type=3,
            required=True
        ),
        create_option(
            name="reason",
            description="Reason for nickname.",
            option_type=3,
            required=False
        ),
    ]
)
async def rename(ctx,target,nickname:str,reason="N/A"):
    print(type(target))
    print(type(ctx.author))
    author = ctx.author
    msg = ctx.message
    await renameModule.rename_target(ctx,msg,author,target,nickname,reason)

@slash.slash(
    name="getnicknames",
    description="Return a list of nicknames given to this loser.",
    options=[
        create_option(
            name="target",
            description="User to look up nicknames for.",
            option_type=6,
            required=True
        ),
    ]
)
async def getnicknames(ctx,target):
    print(type(target))
    print(type(ctx.author))
    author = ctx.author
    msg = ctx.message
    await renameModule.get_nicknames(ctx,target)

@slash.slash(
    name="addquote",
    description="Immortalize some bullshit some idiot said.",
    options=[
        create_option(
            name="target",
            description="User to add quote for.",
            option_type=6,
            required=True
        ),
        create_option(
            name="quote",
            description="Quote to add.",
            option_type=3,
            required=True
        ),
        create_option(
            name="context",
            description="Context for the quote.",
            option_type=3,
            required=False
        ),
    ]
)
async def addquote(ctx,target,quote,context="N/A"):
    await quotesModule.addquote(ctx,target,quote,context)



@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))

token = ""

with open("credentials.json","r") as file:
    creds = json.load(file)
    token = creds['token']


client.run(token)