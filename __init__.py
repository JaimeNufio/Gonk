import discord
import commands.basekit as shell 
import json

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message): #Handle Messages

        if message.author == self.user:
            return

        await shell.handle(self, message)


token = ""

with open("credentials.json","r") as file:
    creds = json.load(file)
    token = creds['token']

client = MyClient()
client.run(token)