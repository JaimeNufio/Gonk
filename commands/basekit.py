import discord
from . import rename, utils

async def handle(obj, message):

    if message.content[0] != "🐚": #Not a :shell: command
        return

    split = (message.content).lower().split(" ")

    # print(obj)
    # print(message)

    if split[1] == "rename":
        await rename.rename(obj,message)