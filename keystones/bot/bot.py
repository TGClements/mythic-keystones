import discord
from discord.ext import commands
from time import time, asctime, localtime

from keystones.bot import (command_validation,
                           help,
                           messages)

from keystones.external.database_manager import DatabaseManager

from secrets import DISCORD_TOKEN

intents = discord.Intents.all()
description = 'A bot to keep track of mythic keystones'
bot = commands.Bot(command_prefix='!', description=description, intents=intents)
#bot.remove_command('help')
bot.add_cog(help.HelpCog())

db_manager = DatabaseManager('./keystones/external/')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(f'Start running at {asctime(localtime(time()))}')
    print('------')


@bot.command(name='dungeons',
             aliases=['dungeon'],
             pass_context=True)
async def list_dungeons(ctx):
    await ctx.send(messages.list_dungeons())


@bot.command(name='affix',
             pass_context=True)
async def get_affix_details(ctx, affix_name):
    await ctx.send(command_validation.get_affix_details(affix_name))


@bot.command(name='affixes',
             pass_context=True)
async def get_period_affixes(ctx, period_offset="0"):
    await ctx.send(command_validation.get_period_affixes(period_offset))


@bot.command(name='timer',
             aliases=['timers', 'time'],
             pass_context=True)
async def get_dungeon_timers(ctx, *dungeon_name):
    await ctx.send(command_validation.get_dungeon_timers(*dungeon_name))


@bot.command(name='add',
             pass_context=True)
async def add_key(ctx, *args):
    """

    Adds a keystone for the user.

    Requires at least 3 args: a character name, a dungeon name, and
    a dungeon level. The character name must be a single word.
    """
    await ctx.send(command_validation.insert_keystone(ctx, db_manager, *args))

# WIP for removing keystone
@bot.command(name='remove',
	     aliases=['rm'],
	     pass_context=True)
async def remove_key(ctx, *args):
    """
    Removes a keystone for a user's character.

    Requires 1 arg: a character name. The character name must be a single word.
    """
    await ctx.send(command_validation.remove_keystone(ctx, db_manager, *args))

@bot.command(name='get',
             aliases=['keys', 'key', 'keystones', 'keystone'],
             pass_context=True)
async def get_keys(ctx):
    await ctx.send(command_validation.get_keystones(ctx, db_manager))


def main():
    try:
        bot.run(DISCORD_TOKEN)
    finally:
        print(f'End running at {asctime(localtime(time()))}')
