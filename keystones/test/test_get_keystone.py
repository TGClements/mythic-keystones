import unittest
from unittest.mock import MagicMock

from keystones.test.discord_mocks import DiscordMessage, DiscordCtx

from keystones.core.command_validation import get_keystones


class TestGetKeystones(unittest.TestCase):
    def setUp(self):
        self.db_manager = MagicMock()

    def test_no_mentions(self):
        pass

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
