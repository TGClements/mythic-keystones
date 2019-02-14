import discord


def contains_mention_here(message: str):
    return '@here' in message.split()


def contains_mention_everyone(message: str):
    return '@everyone' in message.split()


def contains_here(message: str):
    """ Checks if a string contains @here or similar words """
    target = {'@here', 'here', 'online'}
    message_split = set(message.split())
    return len(target & message_split) > 0


def contains_everyone(message: str):
    """ Checks if a string contains @everyone or similar words """
    target = {'@everyone', 'everyone', 'all'}
    message_split = set(message.split())
    return len(target & message_split) > 0


def get_all_mentioned_users(message: discord.Message):
    """

    Returns a set of all user ids mentioned in a message
    :param message: discord.Message - The message with mentions
    :return: set
    """
    mentioned_users = set()

    everyone = contains_everyone(message.content)
    here = contains_here(message.content)

    # Mentioning everyone makes every other mention obsolete, so it's
    # split into its own case. All other mentions can be combined
    if everyone:
        # Add all users in the server
        mentioned_users.update({member.id for member in
                               message.channel.members})
    elif not message.mentions and not message.role_mentions and not here:
        # No mentions, add only the caller
        mentioned_users.add(message.author.id)
    else:
        if here:
            # Add all users in the server who are not offline
            mentioned_users.update({member.id
                                    for member in message.channel.members
                                    if is_here(member)
                                    })
        if message.role_mentions:
            # Add all users with the mentioned role
            mentioned_users.update({member.id
                                    for role in message.role_mentions
                                    for member in role.members
                                    })
        if message.raw_mentions:
            # Add all directly mentioned users
            # raw_mentions is a list of user ids
            mentioned_users.update(set(message.raw_mentions))

    return mentioned_users


def is_here(member: discord.Member):
    """ Checks if a user would be pinged with @here """
    return str(member.status) != 'offline'


def get_server_members(server: discord.Guild):
    """ Returns a set of user ids for all server members """
    return {member.id for member in server.members}