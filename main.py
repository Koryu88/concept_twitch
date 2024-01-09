import sys

from twitchio.ext import commands

import yamlreader

yml_reader = yamlreader.YamlReader()

TOKEN = str(yml_reader.read_property()["token"])

# The Channel you want to check
CHANNEL = str(yml_reader.read_property()["channel"])

print("Insert win word: ")
# This will contain the win string
WIN_MESSAGE = str(input())


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=TOKEN, prefix='?', initial_channels=[CHANNEL])
        self.channel = self.get_channel(CHANNEL)

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):

        # avoid reading the bot messages
        if message.echo:
            return

        # Print every message in chat
        print(f"User:{message.author.name} - Message:{message.content}")

        # message found
        if message.content.lower().strip() == WIN_MESSAGE.lower():
            print(f"The winner is {message.author.name}")
            await message.channel.send(f"YOU WIN {message.author.name}")

            # close on finish
            await self.close()
            sys.exit()


bot = Bot()
bot.run()
