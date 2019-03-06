from keystones.core.dungeon_utils import get_dungeon_id


def insert_keystone(ctx, db_manager, *args) -> str:
    """
    Attempt to insert a keystone based on a user command.
    :param ctx: (discord.Context) - context object for invoked command
    :param args: (tuple of str) - arguments used for the bot command
    :param db_manager: (DatabaseManager) - manager for db being used
    :return: (str) - message to send to Discord client
    """
    if len(args) < 3:
        return (f"I'm sorry, I didn't understand that. Try `!help "
                f"{ctx.invoked_with}` for help with formatting.")
    character, *dungeon, level = args
    dungeon = sanitize(' '.join(dungeon))
    level = sanitize(level)
    dungeon_id = get_dungeon_id(dungeon)
    if not dungeon_id:
        return (f"I'm sorry, I didn't understand the dungeon `{dungeon}`. "
                f"Try `!help dungeons` for help with dungeon names.")
    if not level.isdigit():
        return f"`{level}` isn't a valid dungeon level; please input a number."
    user_id = ctx.message.author.id
    db_manager.add_keystone(user_id, character, dungeon_id, level)


def sanitize(input: str) -> str:
    """
    Removes backticks (code tag) and linebreaks from an input.
    """
    return input.replace('`', '').replace('\n','')