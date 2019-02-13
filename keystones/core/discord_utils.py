from itertools import chain

import pprint


def contains_mention_here(message):
    return '@here' in message.split()


def contains_mention_everyone(message):
    return '@everyone' in message.split()


def contains_here(message):
    target = {'@here', 'here', 'online'}
    message_split = set(message.split())
    return len(target & message_split) > 0


def contains_everyone(message):
    target = {'@everyone', 'everyone', 'all'}
    message_split = set(message.split())
    return len(target & message_split) > 0


def get_all_mentioned_users(message):
    # message.raw_mentions is a list of user ids.
    # If no users were directly mentioned, then it returns an empty list
    # We use a set to prevent duplicates
    mentioned_users = set()

    # Mentioning everyone makes every other mention obsolete, so it's
    # split into its own case. All other mentions can be combined
    if contains_everyone(message.content):
        # Add all users in the server
        mentioned_users.update({member.id for member in
                               message.channel.members})
    else:
        here = contains_here(message.content)
        if not message.mentions and not message.role_mentions and not here:
            # No mentions, add only the caller
            mentioned_users.add(message.author.id)
        if here:
            # Add all users in the server who are online
            mentioned_users.update({member.id for member in
                                 message.channel.members if is_online(member)})
        if message.role_mentions:
            mentioned_users.update(chain({
                member.id for role in message.role_mentions for member in
                role.members
            }))
        if message.raw_mentions:  # List of user ids, don't need to convert
            mentioned_users.update(set(message.raw_mentions))

    return mentioned_users


def is_online(member):
    return str(member.status) != 'offline'
