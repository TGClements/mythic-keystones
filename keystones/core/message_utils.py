from keystones.core import dungeon_utils


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