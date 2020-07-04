from enum import Enum
from typing import List


class MemberStatus(Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'
    IDLE = 'idle'
    DND = 'dnd'
    DO_NOT_DISTURB = 'dnd'
    INVISIBLE = 'invisible'


class DiscordMember:
    """
    A mock Discord Member object.
    """
    def __init__(self, user_id=1, name='Discord User', **kwargs):
        self.id = user_id
        self.name = name

        self.status = kwargs.get('status', MemberStatus.ONLINE)
        self.display_name = kwargs.get('display_name', self.name)
        self.roles = kwargs.get('roles', [DiscordRole('@everyone', members=[self])])

        for role in self.roles:
            if self not in role.members:
                role.members.append(self)


class DiscordMessage:
    """
    A mock Discord Message object.
    :param content: The message body.
    :param author: DiscordMember or None
    """
    def __init__(self, content: str, author=None, id=1, **kwargs):
        self.content = content
        self.author = author or DiscordMember()
        self.id = id

        self.mentions = kwargs.get('mentions', [])
        self.role_mentions = kwargs.get('role_mentions', [])
        self.channel = kwargs.get('channel', DiscordTextChannel([]))

        self.raw_mentions = [member.id for member in self.mentions]

    def get_args(self) -> List[str]:
        """
        Helper to mock the 'args' parameter. Not a real Message property.
        """
        return self.content.split()[1:]


class DiscordCtx:
    """
    A mock Discord Context object.
    """
    def __init__(self, discord_message: DiscordMessage, **kwargs):
        self.message = discord_message
        self.invoked_with = discord_message.content.split().pop(0)[1:]
        self.author = self.message.author

        self.guild = kwargs.get('guild', DiscordGuild([self.author]))


class DiscordGuild:
    def __init__(self, members):
        self._members = {member.id: member for member in members}

    @property
    def members(self):
        return list(self._members.values())

    def get_member(self, user_id):
        return self._members.get(user_id)


class DiscordTextChannel:
    def __init__(self, members, guild=None):
        self._members = {member.id: member for member in members}
        self.guild = guild or DiscordGuild(members)

    @property
    def members(self):
        return list(self._members.values())

    def get_member(self, user_id):
        return self._members.get(user_id)


class DiscordRole:
    def __init__(self, name, **kwargs):
        self.name = name
        self.members = kwargs.get('members', [])
