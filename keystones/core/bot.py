from discord.ext import commands
from time import time, asctime, localtime

from keystones.core import (command_validation,
                            help,
                            messages)

from keystones.db.database_manager import DatabaseManager

from secrets import DISCORD_TOKEN

description = 'A bot to keep track of mythic keystones'
bot = commands.Bot(command_prefix='!', description=description)
bot.remove_command('help')
bot.add_cog(help.HelpCog())

db_manager = DatabaseManager('./keystones/db/')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(f'Start running at {asctime(localtime(time()))}')
    print('------')

@bot.command(pass_context=True)
async def reset(ctx):
    if ctx.message.author.id == 117092043955765255:
        import keystones.db.db_delete_script
        keystones.db.db_delete_script.main()
    else:
        ctx.send('This command is reserved for Hovsep')

@bot.command(name='dungeons',
             aliases=['dungeon'],
             pass_context=True)
async def list_dungeons(ctx):
    await ctx.send(messages.list_dungeons())

@bot.command(name='affix',
             pass_context=True)
async def get_affix_details(ctx, affix_name):
    await ctx.send(command_validation.get_affix_details(ctx, affix_name))

@bot.command(name='affixes',
             pass_context=True)
async def get_period_affixes(ctx, period_offset=0):
    await ctx.send(command_validation.get_period_affixes(ctx, period_offset))

@bot.command(name='add',
             pass_context=True)
async def add_key(ctx, *args):
    """

    Adds a keystone for the user.

    Requires at least 3 args: a character name, a dungeon name, and
    a dungeon level. The character name must be a single word.
    """
    await ctx.send(command_validation.insert_keystone(ctx, db_manager, *args))


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

