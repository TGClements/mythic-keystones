from typing import List


class DiscordUser:
    """
    A mock Discord User object.
    """
    def __init__(self, user_id=1, name="Discord User"):
        self.id = user_id
        self.name = name


class DiscordMessage:
    """
    A mock Discord Message object.
    """
    def __init__(self, content: str, author=DiscordUser()):
        self.content = content
        self.author = author

    def get_args(self) -> List[str]:
        """
        Helper to mock the 'args' parametre. Not a real Message property.
        """
        return self.content.split(' ')[1:]


class DiscordCtx:
    """
    A mock Discord Context object.
    """
    def __init__(self, discord_message: DiscordMessage):
        self.message = discord_message
        self.invoked_with = discord_message.content.split(' ').pop(0)
