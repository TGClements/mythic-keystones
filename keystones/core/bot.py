from discord.ext import commands
from time import time, asctime, localtime

from keystones.core import discord_utils, message_utils

from discord_token import DISCORD_TOKEN

import pprint

description = 'A bot to keep track of mythic keystones'
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("Start running at " + asctime(localtime(time())))
    print('------')


@bot.command(aliases=['dungeon'], pass_context=True)
async def dungeons(ctx):
    await ctx.send(message_utils.list_dungeons())


@bot.command(name='get', aliases=['keys', 'key', 'keystones', 'keystone'],
             pass_context=True)
async def get_keys(ctx):
    pprint.pprint(discord_utils.get_all_mentioned_users(ctx.message))


def main():
    try:
        bot.run(DISCORD_TOKEN)
        bot.close()
    finally:
        print("End running at " + asctime(localtime(time())))
