from logging import exception
from warnings import catch_warnings
import discord
import re
import json
import random
import traceback
from records import firestore

from datetime import datetime

from discord_slash import context
from . import utils

# :shell: addquote @User "Phrase"
async def addquote(ctx,target,quote,context,by):

    print("Adding quote '{}' from {}".format(quote,target.name))

    #updateQuotesJSON(int(ctx.channel.guild.id),target.id,quote,ctx.channel.guild.name,context,by)
    
    #await updateQuotesJSON(ctx,target,quote,context,by)
    
    await updateQuotesFirebase(ctx,target,quote,context,by)

    #context is a string, the context of the quote.
    #await message.channel.send("Roger Rogger. <@{}>".format(target))


async def updateQuotesFirebase(ctx,target,quote,context,by):

    data = {
            "author":target.id,
            "quote":quote,
            "channel":ctx.channel.id,
            "guild":ctx.guild.id,
            "context":context,
            "historian":by.id,
            "when":str(datetime.now() ),
        }

    print(data)

    try:
        firestore.AddData("Quotes",str(ctx.interaction_id),
            data
        )
        await embededQuoteStore(ctx,data,target,by)
    except Exception as e:
        await ctx.reply("Something Went Wrong!\n```"+repr(e)+"```")
        
async def embededQuoteStore(ctx,obj,target,author):

    print(obj)

    embed=discord.Embed(title="", url=author.avatar_url, color=author.color)
    embed.set_author(name="{} added quote for {}".format(author.display_name,target.display_name), icon_url=author.avatar_url)
    embed.set_thumbnail(url=target.avatar_url)
    embed.add_field(name="{} once said...".format(target.display_name), value=obj['quote'], inline=False)
    if 'context' in obj.keys() and obj['context']:
        embed.add_field(name="Context:", value=obj['context'], inline=False)
    await ctx.send(embed=embed)

#default: random from this server
#optionally: 
async def getQuoteFirebase(ctx,target,client):

    try:

        if target:
            got = firestore.GetQuotes(ctx.guild.id,target.id)
        else:
            got = firestore.GetQuotes(ctx.guild.id)

        print(got)

        if got:
            got = got.to_dict()
        else:
            if target != None:
                print("Failed to find")
                embed=discord.Embed(title="",description="Failed to find a quote for {} in this server! If you think this is an error, go bug Jaime.".format(target.display_name))
                embed.set_author(name="This user has no quotes associated with them.".format(target.display_name,icon_url=target.avatar_url))
                embed.set_thumbnail(url=ctx.guild.splash_url)
            else:
                embed=discord.Embed(title="",description="Failed to find a quote in this server! If you think this is an error, go bug Jaime.")
                # embed.set_author(name="This user has no quotes associated with them.".format(target.display_name,icon_url=target.avatar_url))
                embed.set_thumbnail(url=ctx.guild)
            await ctx.reply(embed=embed)
            return

        userObj = client.get_user(int(got['author']))

        embed=discord.Embed(title="", url=userObj.avatar_url, description=got['quote'],color=ctx.guild.get_member(int(got['author'])).color)
        embed.set_author(name="{} once said...".format(userObj.display_name))
        embed.set_thumbnail(url=userObj.avatar_url)

        if 'context' in got.keys() and got['context']:
            embed.add_field(name="Context", value=got['context'], inline=True)
        await ctx.reply(embed=embed)

    except Exception as e:
        err = traceback.format_exc()
        await ctx.reply((err))

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
        
            embed=discord.Embed(title="",description="Failed to find a quote for {} in this server! If you think this is an error, go bug Jaime.".format(target.display_name))
            embed.set_author(name="This user has no quotes associated with them.".format(target.display_name,icon_url=target.avatar_url))
            embed.set_thumbnail(url=target.avatar_url)

            await ctx.send(embed=embed)
            return

    quoteObj = {}

    print(temp['all'][str(user)])
    quoteObj = random.choice(temp['all'][str(user)])

    userObj = client.get_user(int(user))

    if not userObj:
        embed=discord.Embed(title="",description="Failed to find a quote for {} in this server! If you think this is an error, go bug Jaime.".format(target.display_name))
        embed.set_author(name="This user has no quotes associated with them. (UserObject was None.)".format(target.display_name,icon_url=target.avatar_url))
        embed.set_thumbnail(url=target.avatar_url)


        await ctx.send(embed=embed)
        return

    # TODO use a queue system to keep track of what users (quote?) we have already heard from recently

    embed=discord.Embed(title="", url=userObj.avatar_url, description=quoteObj['quote'],color=ctx.guild.get_member(int(user)).color)
    embed.set_author(name="Found Quote for {}".format(userObj.display_name))
    embed.set_thumbnail(url=userObj.avatar_url)

    if context in quoteObj.keys() and quoteObj['context']:
        embed.add_field(name="Recorded By", value=quoteObj['context'], inline=True)
    await ctx.send(embed=embed)