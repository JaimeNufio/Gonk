import discord
import re
import json
import random
from datetime import datetime
from discord.utils import get
import asyncio

from commands import music


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
    pattern = re.compile("(.)*ye(.)*")
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

async def handleAHH(ctx,bot):
    await music.SummonVoice(ctx,bot,'ahh')

async def handleYUBIYUBI(ctx,bot):
    await music.SummonVoice(ctx,bot,'yubi')

async def handleOther(ctx, bot):
    
    text = ctx.content.lower()

    #AHHHH
    pattern = re.compile("^[Aa]+[Hh]+$")
    if pattern.search(text):

        await ctx.reply("https://cdn.discordapp.com/attachments/779408020856635422/851946253063290930/aaaaahh-256.gif")
        await music.SummonVoice(ctx,bot,'ahh')

    pattern = re.compile("^((yubi)[\s])+")
    if pattern.search(text):
        print("YUBI YUBI")
        possible = [
            "https://c.tenor.com/ytFbGN6IcbcAAAAM/korone.gif",
            "https://i.pinimg.com/originals/cb/2b/d1/cb2bd1e53d29b0fcc6d9b739ca08af98.gif",
            "https://i.pinimg.com/originals/3f/64/12/3f6412b65a797bde9b882bd07c43a244.gif",
            "https://c.tenor.com/jppoy0e0yFsAAAAC/inugami-korone.gif"
            ] 

        await ctx.reply(random.choice(possible))
        await music.SummonVoice(ctx,bot,'yubi')

    pattern = re.compile("^(water in the fire)|^(wh+y+)$")
    if pattern.search(text):
        print("WATER IN THE FIRE")
        possible = [
            "https://c.tenor.com/ytFbGN6IcbcAAAAM/korone.gif",
            "https://i.pinimg.com/originals/cb/2b/d1/cb2bd1e53d29b0fcc6d9b739ca08af98.gif",
            "https://i.pinimg.com/originals/3f/64/12/3f6412b65a797bde9b882bd07c43a244.gif",
            "https://c.tenor.com/jppoy0e0yFsAAAAC/inugami-korone.gif"
            ] 
        await ctx.reply(random.choice(possible))
        await music.SummonVoice(ctx,bot,'waterinthefire')

    #WO[WOwo]+
    pattern = re.compile("^wo[wo]+$")
    if pattern.search(text):
        print("WOWOWOWOWOWO")
        possible = [
            "https://c.tenor.com/ytFbGN6IcbcAAAAM/korone.gif",
            "https://i.pinimg.com/originals/cb/2b/d1/cb2bd1e53d29b0fcc6d9b739ca08af98.gif",
            "https://i.pinimg.com/originals/3f/64/12/3f6412b65a797bde9b882bd07c43a244.gif",
            "https://c.tenor.com/jppoy0e0yFsAAAAC/inugami-korone.gif"
            ] 
        await ctx.reply(("WOW"+ ("OW"*(int(len(text)/2)))) +"\n"+random.choice(possible))
        await music.SummonVoice(ctx,bot,'wow',len(text))

    pattern = re.compile("(.*come.*)|(.*cum.*)")
    patternForce = re.compile(".*cum.*")
    if (pattern.search(text) and random.random() > .85) or patternForce.search(text):
        possible = [
            "https://i.ytimg.com/vi/adF2yzBRMEI/maxresdefault.jpg",
            "https://i.pinimg.com/474x/b2/b5/0b/b2b50b56bb3141c9b6997ad59b6b8016.jpg",
            "https://i.ytimg.com/vi/-qSJcKoUwWs/maxresdefault.jpg",
            "http://geekxgirls.com/images/_articles2/cyberpunk-2077-memes-02.jpg",
            "https://i.kym-cdn.com/entries/icons/original/000/030/115/cover4.jpg",
            "https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png",
            "https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png","https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png","https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png","https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png","https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png","https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png","https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png","https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png","https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png","https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png","https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png","https://www.cnet.com/a/img/2XrAF_OvmrPgyVrmc-VdTrdluFQ=/2019/06/09/fd028156-e5c5-401f-820a-57f5fa32338e/cyberpunk-2077-keanu-reeves-glasses-e3.png",
            ] 

        pattern1 = re.compile(".*(?=com)|.*(?=cum)")    
        # trigger = text.find(pattern1.search(text).group(0))
        # print( trigger[0])
        trigger=""

        await ctx.reply((trigger.upper()+" CUM \n"+random.choice(possible)))
        await music.SummonVoice(ctx,bot,'cum',len(text))


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


    #happy birthday!
    pattern = re.compile("(happy birthday|hbd)")
    if pattern.search(text.lower()):
        itt = int((random.random()*20) + 100)
        sum = "**Happy Birthday "+target.mention+"!**\n"
        items = ['🎉','✨','🥳','🎈','🎇','🎊','🎆']
        for i in range(itt):
            sum += random.choice(items)
        
        await ctx.reply(sum)


