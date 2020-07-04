import unittest
from unittest.mock import MagicMock, patch, PropertyMock

from keystones.test.discord_mocks import DiscordMessage, DiscordCtx, DiscordMember, DiscordTextChannel, DiscordRole

from keystones.bot.command_validation import get_keystones


@patch('keystones.external.blizzard_api.BlizzardAPI.current_period', PropertyMock(return_value=1))
class TestGetKeystones(unittest.TestCase):
    def setUp(self):
        self.db_manager = MagicMock()

    def test_no_mentions(self):
        author = DiscordMember(1, 'Hovsep')
        channel = DiscordTextChannel([author])
        message = DiscordMessage('!keys', author, channel=channel)
        ctx = DiscordCtx(message)

        self.db_manager.get_keystones = MagicMock(return_value={1: [('toon', 245, 10)]})

        result = get_keystones(ctx, self.db_manager)
        self.db_manager.get_keystones.assert_called_with({1}, 1)
        self.assertEqual(result, 'Hovsep\'s keystones:\n   toon: Freehold 10')

    def test_single_mention(self):
        author = DiscordMember(1, 'Hovsep')
        mentioned_user = DiscordMember(2, 'John')
        channel = DiscordTextChannel([author, mentioned_user])
        message = DiscordMessage('!keys @John', author, channel=channel, mentions=[mentioned_user])
        ctx = DiscordCtx(message, guild=channel.guild)

        self.db_manager.get_keystones = MagicMock(return_value={2: [('toon', 245, 10)]})

        result = get_keystones(ctx, self.db_manager)
        self.db_manager.get_keystones.assert_called_with({2}, 1)
        self.assertEqual(result, 'John\'s keystones:\n   toon: Freehold 10')

    def test_multiple_mentions(self):
        author = DiscordMember(1, 'Hovsep')
        mentioned_users = [DiscordMember(2, 'John'), DiscordMember(3, 'Mike')]
        channel = DiscordTextChannel([author] + mentioned_users)
        message = DiscordMessage('!keys @John', author, channel=channel, mentions=mentioned_users)
        ctx = DiscordCtx(message, guild=channel.guild)

        self.db_manager.get_keystones = MagicMock(return_value={
            2: [('toon', 245, 10)],
            3: [('warrior', 251, 12)],
        })

        result = get_keystones(ctx, self.db_manager)
        self.db_manager.get_keystones.assert_called_with({2, 3}, 1)
        self.assertEqual(result, 'John\'s keystones:\n   toon: Freehold 10\n'
                                 'Mike\'s keystones:\n   warrior: The Underrot 12')

    def test_mention_everyone(self):
        author = DiscordMember(1, 'Hovsep')
        users = [author, DiscordMember(2, 'John'), DiscordMember(3, 'Mike')]
        channel = DiscordTextChannel(users)
        message = DiscordMessage('!keys @everyone', author, channel=channel)
        ctx = DiscordCtx(message, guild=channel.guild)

        self.db_manager.get_keystones = MagicMock(return_value={
            1: [('pally', 246, 15)],
            2: [('toon', 245, 10)],
            3: [('warrior', 251, 12)],
        })

        result = get_keystones(ctx, self.db_manager)
        self.db_manager.get_keystones.assert_called_with({1, 2, 3}, 1)
        self.assertEqual(result, 'Hovsep\'s keystones:\n   pally: Tol Dagor 15\n'
                                 'John\'s keystones:\n   toon: Freehold 10\n'
                                 'Mike\'s keystones:\n   warrior: The Underrot 12')

    def test_mention_here(self):
        author = DiscordMember(1, 'Hovsep')
        users = [author, DiscordMember(2, 'John'), DiscordMember(3, 'Mike', status='offline')]
        channel = DiscordTextChannel(users)
        message = DiscordMessage('!keys @here', author, channel=channel)
        ctx = DiscordCtx(message, guild=channel.guild)

        self.db_manager.get_keystones = MagicMock(return_value={
            1: [('pally', 246, 15)],
            2: [('toon', 245, 10)],
        })

        result = get_keystones(ctx, self.db_manager)
        self.db_manager.get_keystones.assert_called_with({1, 2}, 1)
        self.assertEqual(result, 'Hovsep\'s keystones:\n   pally: Tol Dagor 15\n'
                                 'John\'s keystones:\n   toon: Freehold 10')

    def test_mention_role(self):
        mention_role = DiscordRole('role')
        general_role = DiscordRole('@everyone')
        author = DiscordMember(1, 'Hovsep', roles=[general_role])
        users = [
            author,
            DiscordMember(2, 'John', roles=[mention_role, general_role]),
            DiscordMember(3, 'Mike', roles=[general_role])
        ]
        channel = DiscordTextChannel(users)
        message = DiscordMessage('!keys @role', author, channel=channel, role_mentions=[mention_role])
        ctx = DiscordCtx(message, guild=channel.guild)

        self.db_manager.get_keystones = MagicMock(return_value={
            2: [('toon', 245, 10)],
        })

        result = get_keystones(ctx, self.db_manager)
        self.db_manager.get_keystones.assert_called_with({2}, 1)
        self.assertEqual(result, 'John\'s keystones:\n   toon: Freehold 10')

    def test_mention_role_and_user(self):
        mention_role = DiscordRole('role')
        general_role = DiscordRole('@everyone')
        author = DiscordMember(1, 'Hovsep', roles=[general_role])
        mentioned_user = DiscordMember(3, 'Mike', role=[general_role])
        users = [
            author,
            DiscordMember(2, 'John', roles=[mention_role, general_role]),
            mentioned_user
        ]
        channel = DiscordTextChannel(users)
        message = DiscordMessage('!keys @role @Mike', author, channel=channel,
                                 role_mentions=[mention_role], mentions=[mentioned_user])
        ctx = DiscordCtx(message, guild=channel.guild)

        self.db_manager.get_keystones = MagicMock(return_value={
            2: [('toon', 245, 10)],
            3: [('warrior', 251, 12)],
        })

        result = get_keystones(ctx, self.db_manager)
        self.db_manager.get_keystones.assert_called_with({2, 3}, 1)
        self.assertEqual(result, 'John\'s keystones:\n   toon: Freehold 10\n'
                                 'Mike\'s keystones:\n   warrior: The Underrot 12')

    def test_db_error(self):
        author = DiscordMember(1, 'Hovsep')
        channel = DiscordTextChannel([author])
        message = DiscordMessage('!keys', author, channel=channel)
        ctx = DiscordCtx(message)

        self.db_manager.get_keystones = MagicMock(return_value=None)

        result = get_keystones(ctx, self.db_manager)
        self.db_manager.get_keystones.assert_called_with({1}, 1)
        self.assertEqual(result, 'There was a problem getting the keystones.')
