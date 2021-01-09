import discord
import re
import json
from . import utils

async def rename(self, message):

    if message.mentions[0] == message.author:
         await message.channel.send('Can\'t rename yourself!')
    
    target = message.mentions[0].id
    matches = re.search('\".*\"',message.content)
 
    if matches:
        name = matches[0][1:-1]
        if len(name) > 32:
            await message.reply('Nickname is {} characters too long! (Maximum length is 32 Characters.)'.format(len(name)-32))
            return

        print("Will rename user to {}".format(name))
        await message.mentions[0].edit(nick=name)
        #await message.reply(content='{}\'s nickname was updated to "{}".'.format(curr,name),mention_author=True)
        await message.channel.send(content='{}\'s nickname was updated to "{}".'.format(target,name))

        utils.updateNickNamesJSON(message.channel.guild.id,target,name)
    