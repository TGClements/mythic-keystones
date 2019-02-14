from discord.ext import commands
from time import time, asctime, localtime

from keystones.core import discord_utils, dungeon_utils

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


@bot.command(aliases=['dungeon'])
async def dungeons():
    """

    Says the names of all dungeons and some of their
    accepted alternative names.
    :return: None
    """
    names = dungeon_utils.EXAMPLE_NAMES
    formatted_names = []
    for name in names:
        alternative_names = ', '.join(names[name])
        formatted_names.append(f'{name}: {alternative_names}')

    header = 'Here are the dungeons and some of their alternative names:\n'
    dungeons = '\n'.join(formatted_names)

    message = f'{header}```{dungeons}```'
    await bot.say(message)


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
