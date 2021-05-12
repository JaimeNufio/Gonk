import discord
from . import utils
from . import quotes
from . import rename

async def handle(obj, message):

    split = (message.content).lower().split(" ")

    # print(obj)
    # print(message)

    if split[1] == "rename":
        await rename.rename(obj,message)

    if split[1] == "addquote":
        await quotes.addquote(obj,message)

    #option to specify user.
    #option to specify server.
    if split[1] == "randomquote":
        await quotes.randomquote(obj,message)