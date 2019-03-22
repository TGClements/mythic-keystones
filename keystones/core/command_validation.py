import re

from keystones.core import dungeon_utils, messages, discord_utils


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

    keystone = (ctx.author.id, character, dungeon_id, level)
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


def get_keys(ctx, db_manager):
    mentioned_users = discord_utils.get_all_mentioned_users(ctx.message)
    keys = db_manager.get_keystones_many(mentioned_users)
    # None signifies an error. `not keys` would be true when the
    # mentioned users don't have keystones in the db
    if keys is None:
        return f'There was a problem getting your keystones.'

    message = messages.format_user_keys(ctx.guild, keys)
    return message


def sanitize(message: str) -> str:
    """
    Removes backticks (code tag) and linebreaks from a message.
    """
    return message.replace('`', '').replace('\n', '')
