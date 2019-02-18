from keystones.core.dungeon_utils import get_dungeon_id


def insert_keystone(ctx, args, db_manager) -> str or None:
    """
    Attempt to insert a keystone based on a user command.
    :param ctx: Discord Context object for a message
    :param args: The arguments following a bot command prefix
    :param db_manager: DatabaseManager
    :return: str error if it was an invalid input; None if it was valid.
    """
    if len(args) < 3:
        return (f"I'm sorry, I didn't understand that. Try `!help "
                f"{ctx.invoked_with}` for help with formatting.")
    character, *dungeon, level = args
    dungeon = ' '.join(dungeon)
    dungeon_id = get_dungeon_id(dungeon)
    if not dungeon_id:
        return (f"I'm sorry, I didn't understand the dungeon `{dungeon}`. "
                f"Try `!help dungeons` for help with dungeon names.")
    if not level.isdigit():
        return f"`{level}` isn't a valid dungeon level; please input a number."
    user_id = ctx.message.author.id
    db_manager.add_keystone(user_id, character, dungeon_id, level)
