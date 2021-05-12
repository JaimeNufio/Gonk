import discord
import re
import json
import random
from datetime import datetime
from . import utils

# :shell: addquote @User "Phrase"
async def addquote(ctx,target,quote,context):

    print("Adding quote '{}' from {}".format(quote,target.name))

    updateQuotesJSON(int(ctx.channel.guild.id),target.id,quote,ctx.channel.guild.name,context)

    embed=discord.Embed(color=0xfa0000)
    embed.set_thumbnail(url=target.avatar_url)
    embed.add_field(name="Added {} Quote:".format(target.display_name), value='*\"{}\"*'.format(quote), inline=True)
    embed.set_footer(text="From Server: \"{}\"".format(ctx.channel.guild.name))
    await ctx.send(embed=embed)

    #await message.channel.send("Roger Rogger. <@{}>".format(target))

# :shell: randomquote [@User] [any]
async def randomquote(self, message):

    random.seed()

    #search any server known to bot? [TODO is this to powerful?]
    anyServer = utils.options(message.content,"any")

    thisServer = message.channel.guild.id

    ####    Begin Searching Through Quotes   #####################################

    temp = {}

    with open("././records/quotes.json","r") as file:
        temp = json.load(file)

    #For the moment, only pull from this Server. Don't acknowledge "any" or @

    ServerToSearch = str(message.channel.guild.id)

    memberID = ""
    
    #which user to care about, if any.
    if len(message.mentions) > 0:

        target = str(message.mentions[0].id)
        #print(list(temp[ServerToSearch]['users'].keys()))

        #Condition that Target Specified, but no quotes found
        if target not in list(temp[ServerToSearch]['users'].keys()):
            print("User has no quotes in the server!")

            embed=discord.Embed(color=0xfa0000)
            embed.set_thumbnail(url=message.mentions[0].avatar_url)
            embed.add_field(name="No Quotes Found For {}!".format(message.mentions[0].display_name), value="You should add one though!", inline=True)
            #embed.set_footer(text="")
            
            await message.channel.send(embed=embed)
            return

        memberID = target

    #choose memeber at random, with the assumption
    else:
        memberID = random.choice(list(temp[ServerToSearch]['users'].keys()))

    ##############################################################################
    
    #Get Information about User from memberID
    #print(memberID)
    found = random.choice(temp[ServerToSearch]['users'][memberID]['quotes'])
    found.append(memberID)
    found.append(temp[ServerToSearch]['meta']['name'])

    user = discord.utils.get(message.channel.guild.members,id=int(found[2]))
    #print(message.channel.members)

    print(user)
    embed=discord.Embed(color=0xfa0000)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="{} Quote:".format(user.display_name), value='\"{}\"'.format(found[0]), inline=True)
    embed.set_footer(text="Quote Added On: {}".format(utils.prettydate(found[1])))
    await message.channel.send(embed=embed)

        

def updateQuotesJSON(serverID,memberID,quote,serverName,context):
    temp = {}

    serverID = str(serverID)
    memberID = str(memberID)
    quote = str(quote)
    
    with open("././records/quotes.json","r") as file: 
        temp = json.load(file)

    with open("././records/quotes.json","w") as file:


        if serverID not in temp.keys():
            print("Server [{}] is unknown to bot.".format(serverID))
            temp[serverID] = {}
            temp[serverID]['meta'] = {}
            temp[serverID]['meta']['name'] = serverName
            temp[serverID]['users'] = {}


        if 'all' not in temp[serverID].keys():
            temp[serverID]['all'] = []
            
        if memberID not in temp[ serverID ]['users'].keys():
            print("Member [{}] is unknown in server.".format(memberID))
            temp[ serverID ]['users'][ memberID ] = {}

        if "quotes" not in temp[ serverID ]['users'][ memberID ].keys():
            print("Member [{}] doesn't have a quote list.".format(memberID))
            temp[ serverID ]['users'][ memberID ]['quotes'] = []
            temp[ serverID ]['users'][ memberID ]['context'] = []

        temp[ serverID ]['users'][ memberID ]['context'].append(context)
        temp[ serverID ]['users'][ memberID ]['quotes'].append( tuple([quote,str(datetime.now())]) )
        temp[serverID]['all'].append( tuple([quote,memberID,str(datetime.now())]) )

        json.dump(temp,file,indent=2)
