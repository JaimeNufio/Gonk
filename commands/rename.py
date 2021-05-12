import discord
import re
import json

from discord import message
from . import utils

async def rename_target(ctx,msg,author,target,nickname,reason="N/A"):

    print(target.name+" ? "+author.name)

    if target.name == author.name:
        await ctx.send('Can\'t rename yourself!')
        return
 
    if nickname:
        if len(nickname) > 32:
            await ctx.send('Nickname is {} characters too long! (Maximum length is 32 Characters.)'.format(len(nickname)-32))
            return

        print("Will rename user to {}".format(nickname))
        await target.edit(nick=nickname)
        await ctx.send(content='{}\'s nickname was updated to "{}". \nReason: {}'.format(target.name,nickname,reason))

        updateNickNamesJSON(ctx.channel.guild.id,target.id,nickname,reason,ctx.guild.name)

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
   
def updateNickNamesJSON(serverID,memberID,name,reason,serverName):
    temp = {}

    serverID = str(serverID)
    memberID = str(memberID)
    name = str(name)
    reason = str(reason)
    
    with open("././records/names.json","r") as file: 
        temp = json.load(file)

    with open("././records/names.json","w") as file:

        if serverID not in temp.keys():
            print("Server [{}] is unknown to bot.".format(serverID))
            temp[ serverID ] = {}
            temp[serverID]['meta'] = {}
            temp[serverID]['meta']['name'] = serverName

        if memberID not in temp[ serverID ].keys():
            print("Member [{}] is unknown in server.".format(memberID))
            temp[ serverID ][ memberID ] = {}

        if "nicknames" not in temp[ serverID ][ memberID ].keys():
            print("Member [{}] doesn't have a nickname list.".format(memberID))
            temp[ serverID ][ memberID ]['nicknames'] = []
            temp[ serverID ][ memberID ]['reasons'] = []

        temp[ serverID ][ memberID ]['nicknames'].append( name )
        temp[ serverID ][ memberID ]['reasons'].append( reason )

        json.dump(temp,file,indent=2)