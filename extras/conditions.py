import discord
import re
import json
import random
from datetime import datetime
from discord.utils import get


tone = "182586772876689419"
amish = "153357620911144960"

async def handleEmoji(ctx,bot):

    text = ctx.content

    #No
    pattern = re.compile("^(:)?[nN][oO](.)?(:)?$")
    if pattern.search(text):
        emoji = get(bot.emojis, name='no')
        await ctx.add_reaction(emoji)

    #Yes
    pattern = re.compile("^(:)?[Yy][e][s](.)?(:)?$")
    if pattern.search(text):
        emoji = get(bot.emojis, name='yes')
        await ctx.add_reaction(emoji)

    #kanye
    pattern = re.compile("(.)*kanye(.)*")
    if pattern.search(text):
        emoji = get(bot.emojis, name='kanye')
        await ctx.add_reaction(emoji)

    #gamers
    pattern = re.compile("(.)*gamers(.)*")
    if pattern.search(text):
        emoji = get(bot.emojis, name='gamer')
        await ctx.add_reaction(emoji)

    #ayy
    pattern = re.compile("^ay(y)+$")
    if pattern.search(text):
        emoji = get(bot.emojis, name='glory')
        await ctx.add_reaction(emoji)

    #hrm
    pattern = re.compile("^h(r)?(m)*(n)*$")
    if pattern.search(text):
        emoji = "🤔" #get(bot.emojis, name='thinking')
        await ctx.add_reaction(emoji)

    #VOTE:
    pattern = re.compile("^vote(.)*:")
    if pattern.search(text):
        emoji = "👍" #get(bot.emojis, name='thumbsup')
        await ctx.add_reaction(emoji)
        emoji = "👎" #get(bot.emojis, name='thumbsdown')
        await ctx.add_reaction(emoji)

    #amish
    pattern = re.compile("AM(I)+(S)+H")
    if pattern.search(text):
        emoji = get(bot.emojis, name='NadeRave')
        await ctx.add_reaction(emoji)
        emoji = get(bot.emojis, name='partykirby')
        await ctx.add_reaction(emoji)
        emoji = get(bot.emojis, name='pepedance')
        await ctx.add_reaction(emoji)
        emoji = get(bot.emojis, name='spin')
        await ctx.add_reaction(emoji)
        emoji = get(bot.emojis, name='NRGparty')
        await ctx.add_reaction(emoji)
        emoji = get(bot.emojis, name='birbparty')
        await ctx.add_reaction(emoji)
        emoji = get(bot.emojis, name='NRGparty')
        await ctx.add_reaction(emoji)


async def handleOther(ctx, bot):
    
    text = ctx.content

    pattern = re.compile("^[Aa]+[Hh]+$")
    if pattern.search(text):
        print("Test")
        # await ctx.channel.send(";;play https://www.youtube.com/watch?v=gK6B7wweIWs")
        await ctx.reply("https://cdn.discordapp.com/attachments/779408020856635422/851946253063290930/aaaaahh-256.gif")



    if len(ctx.mentions) < 1:
        return #Don't bother, these actions require at least a mention

    target = ctx.mentions[0]

    #AMISH
    emotes=['NadeRave','partykirby','pepedance','spin','NRGparty','bribparty']
    emotes = random.shuffle(emotes)
    if str(target.id) == amish:
        for emote in emotes:
            emoji = get(bot.emojis, name=emote)
            await ctx.add_reaction(emoji)


    #AMOGUS
    pattern = re.compile("is sus$")
    if pattern.search(text):
        if random.random() > .5 or str(target.id) == tone:
            await ctx.reply(
                " .      　。　　　　•　    　ﾟ　　。　　.　　　.　　　.　　　.　\n" \
                "　　.　　　.　　　  　　.　　　　　。　　   。　. 　ﾟ　　　.　  \n" \
                "　.　　      。　                   ඞ   。　    .    • .      　。　　　•\n" \
                "                         <@"+str(target.id)+"> was the imposter.　          　\n" +
                "　。　　 　　　　ﾟ　　　.　    　　　. 　。　　 　　　　ﾟ　　　.　   \n" \
                "    ,　　　　.　 .　　       . 。　　   。　. 　ﾟ　　　.　 。　　  \n" \
                )
        else:
            await  ctx.reply(
                " .      　。　　　　•　    　ﾟ　　。　　.　　　.　　　.　　　.　\n" \
                "　　.　　　.　　　  　　.　　　　　。　　   。　. 　ﾟ　　　.　  \n" \
                "　.　　      。　                  ඞ   。　    .    • .      　。　　　•\n" \
                "                          <@"+str(target.id)+"> was not the imposter.　       　\n" +
                "　。　　 　　　　ﾟ　　　.　    　　　. 　。　　 　　　　ﾟ　　　.　   \n" \
                "    ,　　　　.　 .　　       . 。　　   。　. 　ﾟ　　　.　 。　　  \n" \
            )

