from logging import exception
import discord
from discord import message
from discord.ext.commands import context
import commands.basekit as shell 
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import json

from commands import utils
from commands import quotes as quotesModule
from commands import rename as renameModule
from extras import conditions as extras
from records import firestore
from extras import sus

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


#rename
@slash.slash(
    name="rename",
    # guild_ids=guild_ids,
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

async def rename(ctx,target,nickname:str,reason=""):
    print(type(target))
    print(type(ctx.author))
    author = ctx.author
    msg = ctx.message
    await renameModule.rename_target(ctx,author,target,nickname,reason)

@slash.slash(
    # guild_ids=guild_ids,
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
    await renameModule.get_nicknames(ctx,target)

@slash.slash(
    # guild_ids=guild_ids,
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
async def addquote(ctx,target,quote,context=""):
    print(quote)
    await quotesModule.addquote(ctx,target,quote,context,ctx.author)

@slash.slash(
    name="getquote",
    # guild_ids=guild_ids,
    description="Look back on the best things people said.",
    options=[
        # create_option(
        #     name="where",
        #     description="Consider quotes from all known servers?",
        #     option_type=3,
        #     required=True,
        #     choices=[
        #     create_choice(
        #         name="This Server Only",
        #         value="0"
        #     ),
        #     create_choice(
        #         name="Known Servers",
        #         value="1"
        #     )
        # ]),
        create_option(
            name="target",
            description="Specify a user. If not, will be random.",
            option_type=6,
            required=False
        )
    ]
)
async def getquote(ctx,target=None,where="0"):

    print(where,target)
    await quotesModule.getQuoteFirebase(ctx,target,client)
    # if where == "0":
    #     print("Get quote here")
    #     await quotesModule.getquotehere(ctx,target,client)
    # else:
    #     await quotesModule.getquoteall(ctx,target,client)

@slash.slash(
    # guild_ids=guild_ids,
    name="amogus",
    description="This is dumb. Blame Amish. I mean Jaime implemented, it but fuck amish lol.",
    options=[
        create_option(
            name="url",
            description="Image Url",
            option_type=3,
            required=True
        ),
        create_option(
            name="size",
            description="Width, Ideally 0 to 30, but you can try bigger. Might fail for larger values.",
            option_type=4,
            required=False
        ),
    ]
)
async def amogus(ctx,url,size=30):
    await sus.sus(ctx,url,size)



@client.event
async def on_message(message):

    if message.author.bot:
        print("A bot spoke, ignoring.")
        return
    
    print(message.content)

    #lets handle things like emojis
    await extras.handleEmoji(message,client)
    await extras.handleOther(message,client)

    firestore.AddData("Messages",str(message.id),{
        "author":message.author.id,
        "channel":message.channel.id,
        "guild":message.guild.id,
        "content":message.content,
        "embeded":str(message.embeds),
        "attachments":str(message.attachments),
        "jump_url":message.jump_url,
        "datetime":message.created_at,
    })

@client.event
async def on_ready():
    firestore.init('firebase.json')
    print('Logged on as {0}!'.format(client.user))

client.run(token)
