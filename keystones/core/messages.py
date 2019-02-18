import discord

from keystones.core import dungeon_utils, discord_utils


def list_dungeons():
    """

    Returns a helpful message with the names of all dungeons
    and some of their accepted alternative names.
    :return: str
    """
    names = dungeon_utils.EXAMPLE_NAMES
    formatted_names = []
    for name in names:
        alternative_names = ', '.join(names[name])
        formatted_names.append(f'{name}: {alternative_names}')

    header = 'Here are the dungeons and their alternative names. ' \
             'Note that all names are case insensitive.\n'
    dungeons = '\n'.join(formatted_names)

    return f'{header}```{dungeons}```'


def format_user_keys(server: discord.Guild, keys: dict):
    key_strings = []
    for user_id in keys:
        if not keys[user_id]:
            continue

        user_name = discord_utils.get_member(server, user_id).display_name
        user_header = f'{user_name}\'s keystones:\n'
        user_keys = '\n'.join([
            f'   {character}: '
            f'{dungeon_utils.get_dungeon_name(dungeon)} {level}'
            for character, dungeon, level in keys[user_id]
        ])
        key_strings.append(user_header + user_keys)
    return '\n'.join(key_strings)
