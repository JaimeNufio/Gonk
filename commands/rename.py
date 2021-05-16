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
    items = utils.gatherUserByID(target.id)
    print(items)
    output = "Nicknames found for {}:\n".format(target.name)

    try:
        for i in range(len(items[0])):
            output+="{} - {}\n".format(items[0][i],items[1][i])
        await ctx.send(output)
    except:
        await ctx.send("An error occured, chances are there just aren't nicknames for this user.\n\
        idk. Bug Jaime about this.")
   
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
    embed.set_author(name="{} renamed {}".format(author.display_name,obj['currentname']), icon_url=author.avatar_url)
    embed.set_thumbnail(url=target.avatar_url)

    if "currentname" in obj.keys():
        embed.add_field(name="Previous Name:", value=obj['currentname'], inline=True)
    embed.add_field(name="New Name:", value=obj['nickname'], inline=True)
    await ctx.send(embed=embed)