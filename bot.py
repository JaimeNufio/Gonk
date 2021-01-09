import discord
import commands.basekit as shell 

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message): #Handle Messages

        if message.author == self.user:
            return

        await shell.handle(self, message)


client = MyClient()
client.run('NzkzMTUyMzI2NjQxNjQ3NjU2.X-oGqg.beni3vCM4AgaXu8bGWI3dDAGqhw')