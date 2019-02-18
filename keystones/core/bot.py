from discord.ext import commands
from time import time, asctime, localtime

from keystones.core import discord_utils, messages, dungeon_utils

from keystones.db.database_manager import DatabaseManager

from discord_token import DISCORD_TOKEN

import pprint

description = 'A bot to keep track of mythic keystones'
bot = commands.Bot(command_prefix='!', description=description)

database_manager = DatabaseManager('./db/')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("Start running at " + asctime(localtime(time())))
    print('------')


@bot.command(aliases=['dungeon'], pass_context=True)
async def dungeons(ctx):
    await ctx.send(messages.list_dungeons())


@bot.command(name='add', pass_context=True)
async def add_key(ctx, *args):
    """

    Adds a keystone for the user.

    Requires at least 3 args: a character name, a dungeon name,
    and a dungeon level. The character name can't have spaces.
    """
    # TODO: Add error handling
    # Restrictions on character names? Probably should prevent @ to avoid
    # mention trolling
    if len(args) < 3:
        # Needs a character, dungeon, and key level
        await ctx.send(f'I\'m sorry, I didn\'t understand that. Try `!help '
                       f'{ctx.invoked_with}` for help with formatting.')
        return

    character, *dungeon, level = args
    dungeon = ' '.join(dungeon)

    dungeon_id = dungeon_utils.get_dungeon_id(dungeon)
    if dungeon_id is None:
        await ctx.send('I\'m sorry, I didn\'t understand that dungeon. Try '
                       '`!help dungeons` for help with dungeon names.')
        return

    database_manager.add_keystone((ctx.author.id, character, dungeon, level))
    await ctx.send(f'Added {dungeon} {level} for {character}')


@bot.command(name='get', aliases=['keys', 'key', 'keystones', 'keystone'],
             pass_context=True)
async def get_keys(ctx):
    mentioned_users = discord_utils.get_all_mentioned_users(ctx.message)
    keys = database_manager.get_keystones_many(mentioned_users)
    string = messages.format_user_keys(ctx.guild, keys)
    await ctx.send(string)


def main():
    try:
        bot.run(DISCORD_TOKEN)
        bot.close()
    finally:
        print("End running at " + asctime(localtime(time())))

