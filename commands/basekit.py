from random import random
import discord
from . import utils
from . import quotes
from . import rename
import json
import re


async def beg(ctx):

    x = random()
    print(x)

    if x > .85:
        await ctx.reply("This bot supports Slash Commands! You should try them out!")

async def dollar(ctx,client):
    pass
    # with open("././records/dollar.json","r") as file: 

    #     temp = json.load(file)

    #     try:
    #         target = ctx.message.mentions[0]
    #         if target in temp.keys():
    #             temp[target] += 1
    #         else:
    #             temp[target] = 1

    #         file.write(json.dumps(temp))
            
    #     except:
    #         print("Oopsy Woopsy I made a fucky wucky")


async def handleOld(ctx,client):

    print("handleOld")

    msg = ctx.message.content
    split = msg.split(" ")
    print(split)

    if not (split[0] == "🐚" or split[0] == ":shell:" or split[0] == "shell"):
        return
    else:
        print("Shell Invoked:",msg)

    if split[1] == "rename":

        print(":shell: Rename invoked")
        
        target = ctx.message.mentions[0]
        quote = re.findall(pattern="\".*\"",string=msg)[0][1:-1]
        print("quote:",quote,"\ntarget:",target)
        
        await rename.rename_target(ctx,ctx.author,target,quote,"")
        await beg(ctx)

    elif split[1] == "addquote":
        
        target = ctx.message.mentions[0]
        quote = re.findall(pattern="\".*\"",string=msg)[0][1:-1]
        print("quote",quote)

        await quotes.addquote(ctx,target,quote,"",ctx.author)        
        await beg(ctx)

