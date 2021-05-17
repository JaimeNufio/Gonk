import discord
import re
import json
from datetime import datetime
from discord import message
from . import utils

async def rename_target(ctx,author,target,nickname,reason=""):

    print(target.name+" ? "+author.name)

    currName = target.display_name

    if target.name == author.name:
        await ctx.send('Can\'t rename yourself!')
        return
 
    if nickname:
        if len(nickname) > 32:
            await ctx.send('Nickname is {} characters too long! (Maximum length is 32 Characters.)'.format(len(nickname)-32))
            return

        print("Will rename user to {}".format(nickname))
        await target.edit(nick=nickname)

        await updateNickNamesJSON(ctx,target,nickname,reason,author,currName)

async def get_nicknames(ctx,target):
    names = utils.returnText('names')

    try:
        names = names[str(target.id)]
    except:
        embed=discord.Embed(title="",description="No nicknames were found. If you think this is an error, go bug Jaime.",color=target.color)
        embed.set_author(name="No Previous Names for {}!".format(target.display_name,icon_url=target.avatar_url))
        embed.set_thumbnail(url=target.avatar_url)
        await ctx.send(embed=embed)

    items = ""

    cnt = 0
    for name in names:

        cnt+=1
        items += "{}".format(name['nickname'])

        if len(items) >= 2040:
            items+="."
            break

        elif cnt+1 <= len(names):
            items+=", "
        else:
            items+="."

    embed=discord.Embed(title="",description=items,color=target.color)
    embed.set_author(name="Previous Names for {}:".format(target.display_name,icon_url=target.avatar_url))
    embed.set_thumbnail(url=target.avatar_url)
    await ctx.send(embed=embed)
   
async def updateNickNamesJSON(ctx,target,name,reason,author,currName=""):
    
    temp = {}
    
    serverID = str(ctx.channel.guild.id)
    memberID = str(target.id)
    serverName = ctx.guild.name
    name = str(name)
    reason = str(reason)
    
    with open("././records/names.json","r") as file: 
    
        temp = json.load(file) 

    with open("././records/names.json","w") as file:

        obj = {
            "user":memberID,
            "nickname":name,
            "reason":reason,
            "renamer":str(author.id),
            "when":str(datetime.now() ),
            "serverid":str(serverID),
            "servername":serverName,
            "currentname":currName
        }

        if memberID not in temp.keys():
            temp[memberID] = []

        temp[ memberID ].append( obj )

        json.dump(temp,file,indent=2)

        await embededRenameStore(ctx,obj,target,author)

#Only call when storing, I guess.
async def embededRenameStore(ctx,obj,target,author):

    print(obj)

    embed=discord.Embed(title="", url=author.avatar_url, color=author.color)
    embed.set_author(name="{} renamed {}".format(author.display_name,
        obj['currentname']),
        icon_url=author.avatar_url)
    embed.set_thumbnail(url=target.avatar_url)

    if "currentname" in obj.keys():
        embed.add_field(name="Previous Name:", value=obj['currentname'], inline=True)
    embed.add_field(name="New Name:", value=obj['nickname'], inline=True)
    await ctx.send(embed=embed)