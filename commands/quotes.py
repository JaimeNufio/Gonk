from logging import exception
from warnings import catch_warnings
import discord
import re
import json
import random
from datetime import datetime

from discord_slash import context
from . import utils

# :shell: addquote @User "Phrase"
async def addquote(ctx,target,quote,context,by):

    print("Adding quote '{}' from {}".format(quote,target.name))

    #updateQuotesJSON(int(ctx.channel.guild.id),target.id,quote,ctx.channel.guild.name,context,by)
    await updateQuotesJSON(ctx,target,quote,context,by)
    #context is a string, the context of the quote.


    #await message.channel.send("Roger Rogger. <@{}>".format(target))

# Deprecate?
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

async def updateQuotesJSON(ctx,target,quote,context,by):
    temp = {}

    serverID = str(ctx.channel.guild.id)
    serverName = ctx.channel.guild.name
    memberID = str(target.id)
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


        # if 'all' not in temp[serverID].keys():
        #     temp[serverID]['all'] = []
            
        if memberID not in temp[ serverID ]['users'].keys():
            print("Member [{}] is unknown in server.".format(memberID))
            temp[ serverID ]['users'][ memberID ] = {}

        if "quotes" not in temp[ serverID ]['users'][ memberID ].keys():
            print("Member [{}] doesn't have a quote list.".format(memberID))
            temp[ serverID ]['users'][ memberID ]['quotes'] = []

        obj = {
            "quote":quote,
            "context":context,
            "chronicler":by.id,
            "when":str(datetime.now() ),
            "where":serverName,
        }

        #add super "all" list
        if 'all' not in temp.keys():
            temp['all'] = {}

        if memberID not in temp['all'].keys():
            temp['all'][memberID] = []

        temp['all'][memberID].append(obj)
        # temp[serverID]['all'].append(obj)
        temp[serverID]['users'][memberID]['quotes'].append(obj)

        #temp[ serverID ]['users'][ memberID ]['context'].append(context)
        #temp[ serverID ]['users'][ memberID ]['quotes'].append( tuple([quote,str(datetime.now())]) )
        #temp[serverID]['all'].append( tuple([quote,memberID,str(datetime.now())]) )

        json.dump(temp,file,indent=2)
        await embededQuoteStore(ctx,obj,target,by)

async def embededQuoteStore(ctx,obj,target,author):

    print(obj)
    print(author)
    print(type(author))

    embed=discord.Embed(title="", url=author.avatar_url, color=author.color)
    embed.set_author(name="{} added quote for {}".format(author.display_name,target.display_name), icon_url=author.avatar_url)
    embed.set_thumbnail(url=target.avatar_url)
    embed.add_field(name="Quote Added:", value=obj['quote'], inline=False)
    if 'context' in obj.keys() and obj['context']:
        embed.add_field(name="Context:", value=obj['context'], inline=False)
    await ctx.send(embed=embed)

# consider only quotes in this server
async def getquotehere(ctx,target,client):

    temp = {}
    temp = utils.returnText('quotes')

    thisServer = str(ctx.guild.id) 
    user = ""

    if thisServer not in temp.keys():
        embed=discord.Embed(title="",description="Try the \"All Known Servers\" Option. Legacy quotes are there. If you think this is an error, go bug Jaime.")
        embed.set_author(name="No quotes associated with this server!")
        embed.set_thumbnail(url=client.user.avatar_url)

  
        await ctx.send(embed=embed)
        return      

    #acces User as Key
    if not target:
        try:
            user = random.choice(list(temp[str(thisServer)]['users'].keys()))
            print(user)

            if not user:
                embed=discord.Embed(title="",description="Failed to find a quote for {} in this server! If you think this is an error, go bug Jaime.".format(target.display_name))
                embed.set_author(name="This user has no quotes associated with them here.".format(target.display_name,icon_url=target.avatar_url))
                embed.set_thumbnail(url=target.avatar_url)

                await ctx.send(embed=embed)
                return
                
        except exception as e:
            print("Error: "+e)  
    else:
        user = str(target.id)
        print(user)

        if user not in temp[str(thisServer)]['users'].keys():
        
            embed=discord.Embed(title="",description="Failed to find a quote for {} in this server! If you think this is an error, go bug Jaime.".format(target.display_name))
            embed.set_author(name="This user has no quotes associated with them.".format(target.display_name,icon_url=target.avatar_url))
            embed.set_thumbnail(url=target.avatar_url)

            await ctx.send(embed=embed)
            return

    quoteObj = {}

    print(temp[str(thisServer)]['users'][str(user)]['quotes'])
    quoteObj = random.choice(temp[str(thisServer)]['users'][str(user)]['quotes'])

    userObj = client.get_user(int(user))

    # TODO use a queue system to keep track of what users (quote?) we have already heard from recently

    print(quoteObj)
    print(userObj)

    embed=discord.Embed(title="", url=userObj.avatar_url, description=quoteObj['quote'],color=ctx.guild.get_member(int(user)).color)
    embed.set_author(name="Found Quote for {}".format(userObj.display_name))
    embed.set_thumbnail(url=userObj.avatar_url)

    if context in quoteObj.keys() and quoteObj['context']:
        embed.add_field(name="Recorded By", value=quoteObj['context'], inline=True)
    await ctx.send(embed=embed)

# consider quotes from all
async def getquoteall(ctx,target,client):

    temp = {}
    temp = utils.returnText('quotes')

    user = ""

    #acces User as Key
    if not target:
        try:
            user = str(random.choice(list(temp['all'].keys())))
            print(user)
        except exception as e:
            print("Error: "+e)
    else:
        user = str(target.id)

        if user not in temp['all'].keys():
        
            embed=discord.Embed(title="",description="Failed to find a quote {}! If you think this is an error, go bug Jaime.")
            embed.set_author(name="This user has no quotes associated with them.".format(target.display_name,icon_url=target.avatar_url))
            embed.set_thumbnail(url=target.avatar_url)

            await ctx.send(embed=embed)
            return

    quoteObj = {}

    print(temp['all'][str(user)])
    quoteObj = random.choice(temp['all'][str(user)])

    userObj = client.get_user(int(user))

    # TODO use a queue system to keep track of what users (quote?) we have already heard from recently

    embed=discord.Embed(title="", url=userObj.avatar_url, description=quoteObj['quote'],color=ctx.guild.get_member(int(user)).color)
    embed.set_author(name="Found Quote for {}".format(userObj.display_name))
    embed.set_thumbnail(url=userObj.avatar_url)

    if context in quoteObj.keys() and quoteObj['context']:
        embed.add_field(name="Recorded By", value=quoteObj['context'], inline=True)
    await ctx.send(embed=embed)