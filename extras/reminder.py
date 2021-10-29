import discord
import json
from datetime import datetime, timedelta

async def setReminder(bot,ctx,date,time,zone,message="Reminder!"):

    #Its understandable to leave out the leading 0, let's append
    if len(date) == len("10/13/21")-1:
        date ="0"+date

    try:
        if zone:
            sum = date+" "+time+":00 "+zone
            print(sum)

            dt = datetime.strptime(sum,"%x %X %p")
        else: 
            sum = date+" "+time+":00"
            print(sum)
            dt = datetime.strptime(sum,"%x %X")
    except:
        await ctx.reply("Error Parsing date from {}.".format(sum))
        return

    sumPretty = "{} {} {}".format(date,time,zone if zone else "")

    
    print(dt.utcnow())

    reminder = {
        "when":"" #TODO store as unix?
    }

    await ctx.reply("Set a reminder \"{}\" for {} ({} UTC)".format(message,sumPretty,dt))
    await ctx.author.send("I said this was a __**Work in Progress**__, num nuts.")

async def checkReminders(bot,ctx): 
    pass