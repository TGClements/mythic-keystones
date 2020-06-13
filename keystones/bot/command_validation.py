import re

from keystones.bot import messages
from keystones.utils import affix as affix_utils, discord as discord_utils, dungeon as dungeon_utils
from keystones.external import blizzard_api


def insert_keystone(ctx, db_manager, *args) -> str:
    """
    Attempt to insert a keystone based on a user command.
    :param ctx: (discord.Context) - context object for invoked command
    :param args: (tuple of str) - arguments used for the bot command
    :param db_manager: (DatabaseManager) - manager for db being used
    :return: (str) - message to send to Discord client
    """
    if len(args) < 3:
        # Needs a character, dungeon, and key level
        return (f'I\'m sorry, I didn\'t understand that. Try `!help '
                f'{ctx.invoked_with}` for help with formatting.')

    character = args[0].strip()
    dungeon = sanitize(' '.join(args[1:-1]))
    level = sanitize(args[-1].lstrip('+'))  # Allow +<level> or just <level>

    validation_message = _has_invalid_insertion_args(character, dungeon, level)
    if validation_message:
        return validation_message

    dungeon_id = dungeon_utils.get_dungeon_id(dungeon)
    # The user entered name will likely be an alternative name, but we
    # should use the real name when confirming that the key was added
    dungeon_name = dungeon_utils.get_dungeon_name(dungeon_id)

    blizz_api = blizzard_api.BlizzardAPI.get_instance()
    current_timeperiod = blizz_api.current_period

    keystone = (ctx.author.id, character, dungeon_id, level, current_timeperiod)
    if not db_manager.add_keystone(keystone):
        return (f'There was a problem adding {dungeon_name} +{level} '
                f'for {character}.')

    return f'Added {dungeon_name} +{level} for {character}'


def _has_invalid_insertion_args(character, dungeon, level):
    """

    Checks if the add_key command had invalid arguments
    :param character: (str) character name to associate with a key
    :param dungeon: (str) dungeon name for the key
    :param level: (str) level of the key
    :return: (str or None) A string containing an error message,
              or None if the arguments are all valid
    """
    if not re.match('^[\w-]+$', character):
        return (f'Character names can only contain letters, numbers, '
                f'underscores, and dashes.')

    dungeon_id = dungeon_utils.get_dungeon_id(dungeon)
    if not dungeon_id:
        return (f'I\'m sorry, I didn\'t understand the dungeon `{dungeon}`. '
                f'Try `!dungeons` to see dungeon names.')

    if not level.isdigit() or int(level) < 2:
        return f'`{level}` isn\'t a valid dungeon level.'

    return None


def get_keystones(ctx, db_manager):
    mentioned_users = discord_utils.get_all_mentioned_users(ctx.message)
    blizz_api = blizzard_api.BlizzardAPI.get_instance()
    current_timeperiod = blizz_api.current_period

    keys = db_manager.get_keystones(mentioned_users, current_timeperiod)
    # None signifies an error. `not keys` would be true when the
    # mentioned users don't have keystones in the db
    if keys is None:
        return f'There was a problem getting the keystones.'

    message = messages.format_user_keys(ctx.guild, keys)
    return message


def get_affix_details(ctx, affix_name):
    blizz_api = blizzard_api.BlizzardAPI.get_instance()
    affix_id = affix_utils.get_affix_id(affix_name)
    affix_details = blizz_api.get_affix_details(affix_id)

    return messages.format_affix_details(*affix_details)


def get_period_affixes(ctx, period_offset):
    try:
        period_offset = int(period_offset)
    except ValueError:
        return 'The offset must be an integer between 0 and 11 (inclusive).'
    if period_offset < 0:
        return 'Cannot get past affixes.'
    if period_offset > 11:
        # Only allow one full rotation of affixes
        return 'Cannot get affixes more than 11 weeks into the future.'

    blizz_api = blizzard_api.BlizzardAPI.get_instance()
    affixes = blizz_api.get_affixes_for_timeperiod(blizz_api.current_period + period_offset)
    affix_names = (affix_utils.get_affix_name(affix_id) for affix_id in affixes)

    return messages.format_period_affixes(affix_names)


def get_dungeon_timers(ctx, *dungeon_name):
    if not dungeon_name:
        return 'You must enter a dungeon name. Try `!dungeons` to see dungeon names.'

    dungeon_name = sanitize(' '.join(dungeon_name))
    dungeon_id = dungeon_utils.get_dungeon_id(dungeon_name)
    if not dungeon_id:
        return (f'I\'m sorry, I didn\'t understand the dungeon `{dungeon_name}`. '
                f'Try `!dungeons` to see dungeon names.')
    official_dungeon_name = dungeon_utils.get_dungeon_name(dungeon_id)

    blizz_api = blizzard_api.BlizzardAPI.get_instance()
    timers = blizz_api.get_dungeon_timers(dungeon_id)
    return messages.format_dungeon_timers(official_dungeon_name, timers)


def sanitize(message: str) -> str:
    """
    Removes backticks (code tag) and linebreaks from a message.
    """
    return message.replace('`', '').replace('\n', '')
