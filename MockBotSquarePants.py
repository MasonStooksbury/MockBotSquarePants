#! python3

# MockBotSquarePants.py - A script that handles the functionality of a Discord bot used to mock people

from dotenv import load_dotenv
from discord.ext import commands

import discord

load_dotenv()
# For reasons why you should totally NOT put your Bot-Discord token in here (like I did) and instructions on how to store this better,
# Visit here:     https://realpython.com/how-to-make-a-discord-bot-python/
# To get this token, open the Discord Developer portal, click the "Bot" link on the left, then select "Copy" under the "Token" heading next to the profile picture of your bot.
token = 'DISCORD_TOKEN'


# Uncomment these few lines and you will see a message in the console that let's you know your initial connection worked.
##client = discord.Client()
##@client.event
##async def on_ready():
##    print(f'{client.user} has connected to Discord!')
##client.run(token)


def mockify(normalText):
    mockText = ''

    for index, letter in enumerate(normalText.lower(), start=0):
        if index % 2 == 0:
            mockText += letter
        else:
            mockText += letter.upper()
    return mockText



bot = commands.Bot(command_prefix='~')

@bot.command(name='mock', help='Says your words in the most mocking way possible')
async def mock(ctx, *, message):
    await ctx.send(mockify(message))

bot.run(token)
