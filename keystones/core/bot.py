from discord.ext import commands
from time import time, asctime, localtime

from keystones.core import (command_validation,
                            discord_utils,
                            messages)

from keystones.db.database_manager import DatabaseManager

from discord_token import DISCORD_TOKEN

description = 'A bot to keep track of mythic keystones'
bot = commands.Bot(command_prefix='!', description=description)

db_manager = DatabaseManager('./db/')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("Start running at " + asctime(localtime(time())))
    print('------')


@bot.command(aliases=['dungeon'],
             pass_context=True)
async def dungeons(ctx):
    await ctx.send(messages.list_dungeons())


@bot.command(name='add',
             pass_context=True)
async def add_key(ctx, *args):
    """

    Adds a keystone for the user.

    Requires at least 3 args: a character name, a dungeon name, and
    a dungeon level. The character name must be a single word.
    """
    if ctx.message.author.id != 117092043955765255:
        await ctx.send('Stop griefing')
        return

    message = command_validation.insert_keystone(ctx, db_manager, *args)
    await ctx.send(message)


@bot.command(name='get',
             aliases=['keys', 'key', 'keystones', 'keystone'],
             pass_context=True)
async def get_keys(ctx):
    if ctx.message.author.id != 117092043955765255:
        await ctx.send('Stop griefing')
        return

    await ctx.send(command_validation.get_keys(ctx, db_manager))


def main():
    try:
        bot.run(DISCORD_TOKEN)
        bot.close()
    finally:
        print("End running at " + asctime(localtime(time())))

