class DiscordUser:
    """
    A mock Discord User object.
    """
    def __init__(self):
        self.id = 1
        self.name = "Discord User"


class DiscordMessage:
    """
    A mock Discord Message object.
    """
    def __init__(self, content: str):
        self.author = DiscordUser()
        self.content = content

        # Not a real Message property: helper to mock the 'args' parametre
        self.args = self.content.split(' ')[1:]


class DiscordCtx:
    """
    A mock Discord Context object.
    """
    def __init__(self, discord_message: DiscordMessage):
        self.message = discord_message
        self.invoked_with = discord_message.content.split(' ').pop(0)
