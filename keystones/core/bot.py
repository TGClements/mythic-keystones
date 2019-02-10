import discord
from discord.ext import commands

from discord_token import DISCORD_TOKEN

description = 'A bot to keep track of mythic keystones'
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


def main():
    bot.run(DISCORD_TOKEN)
    bot.close()
