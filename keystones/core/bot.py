from discord.ext import commands

from keystones.core import dungeon_names

from discord_token import DISCORD_TOKEN

description = 'A bot to keep track of mythic keystones'
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(aliases=['dungeon'])
async def dungeons():
    """

    Says the names of all dungeons and some of their
    accepted alternative names.
    :return: None
    """
    names = dungeon_names.EXAMPLE_NAMES
    formatted_names = []
    for name in names:
        alternative_names = ', '.join(names[name])
        formatted_names.append(f'{name}: {alternative_names}')

    header = 'Here are the dungeons and some of their alternative names:\n'
    dungeons = '\n'.join(formatted_names)

    message = f'{header}```{dungeons}```'
    await bot.say(message)


def main():
    bot.run(DISCORD_TOKEN)
    bot.close()
