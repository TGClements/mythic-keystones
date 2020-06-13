from typing import List


class DiscordUser:
    """
    A mock Discord User object.
    """
    def __init__(self, user_id=1, name='Discord User'):
        self.id = user_id
        self.name = name


class DiscordMessage:
    """
    A mock Discord Message object.
    :param content: The message body.
    :param author: DiscordUser or None
    """
    def __init__(self, content: str, author=None, id=1):
        self.content = content
        self.author = author or DiscordUser()
        self.id = id

    def get_args(self) -> List[str]:
        """
        Helper to mock the 'args' parameter. Not a real Message property.
        """
        return self.content.split()[1:]


class DiscordCtx:
    """
    A mock Discord Context object.
    """
    def __init__(self, discord_message: DiscordMessage):
        self.message = discord_message
        self.invoked_with = discord_message.content.split().pop(0)[1:]
        self.author = self.message.author


class DiscordGuild:
    def __init__(self, members):
        self._members = {member.user_id: member for member in members}

    @property
    def members(self):
        return self._members.values()

    def get_member(self, user_id):
        return self._members.get(user_id)
