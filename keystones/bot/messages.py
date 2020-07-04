import discord

from keystones.utils import discord as discord_utils, dungeon as dungeon_utils


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

    if key_strings:
        return '\n'.join(key_strings)
    elif len(keys) == 1:
        user_id = next(iter(keys))
        user_name = discord_utils.get_member(server, user_id).display_name
        return f'There are no keystones for {user_name}.'
    else:
        return 'There are no keystones for the mentioned users.'


def format_affix_details(affix_name, affix_description):
    return f'{affix_name}: {affix_description}'


def format_period_affixes(affixes):
    return ', '.join(affixes)


def format_dungeon_timers(dungeon_name, timers):
    formatted_times = '\n'.join(
        f'+{upgrade_level}: {_format_timer(duration)}'
        for (upgrade_level, duration) in timers.items()
    )
    return f'{dungeon_name} timers:\n{formatted_times}'


def _format_timer(time):
    seconds = time // 1000  # ensure no float
    minutes = seconds // 60
    seconds_leftover = seconds % 60
    extra_zero = '0' if seconds_leftover < 10 else ''

    return f'{minutes}:{extra_zero}{seconds_leftover}'
