import unittest
from unittest.mock import MagicMock, patch

from keystones.test.discord_mocks import DiscordMessage, DiscordCtx, DiscordMember, DiscordTextChannel

from keystones.bot.command_validation import get_keystones


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
        self.assertEqual(result, 'Hovsep\'s keystones:\n   toon: Freehold 10')

    def test_single_mention(self):
        pass

    def test_multiple_mentions(self):
        pass

    def test_mention_everyone(self):
        pass

    def test_mention_here(self):
        pass

    def test_mention_role(self):
        pass

    def test_mention_role_and_user(self):
        pass

    def test_mention_duplicate(self):
        pass

    def test_db_error(self):
        pass
