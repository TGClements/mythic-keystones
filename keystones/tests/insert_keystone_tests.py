import unittest
from unittest.mock import MagicMock

from keystones.core.command_validation import insert_keystone
from keystones.tests.mocks import DiscordMessage, DiscordCtx


class InsertKeystoneTests(unittest.TestCase):
    def test_insert_invalid_dungeon(self):
        user_input = "/addkey Moo dsjdaijdsa 10"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, message.get_args(), MagicMock())
        self.assertEqual(error, f"I'm sorry, I didn't understand the dungeon `dsjdaijdsa`. "
                                f"Try `!help dungeons` for help with dungeon names.")

    def test_insert_invalid_level(self):
        user_input = "/addkey Moo Waycrest NaN"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, message.get_args(), MagicMock())
        self.assertEqual(error, f"`NaN` isn't a valid dungeon level; please input a number.")

    def test_invalid_num_args(self):
        user_input = "/addkey Moo Too"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, message.get_args(), MagicMock())
        self.assertEqual(error, "I'm sorry, I didn't understand that. Try `!help "
                                f"{ctx.invoked_with}` for help with formatting.")

    def test_valid_insertion(self):
        user_input = "/addkey Moo Waycrest 10"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, message.get_args(), MagicMock())
        self.assertIsNone(error)

    def test_valid_insertion_with_spaces(self):
        user_input = "/addkey Moo Waycrest Manor 10"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, message.get_args(), MagicMock())
        self.assertIsNone(error)

    def test_no_character_name(self):
        user_input = "/addkey Temple of Sethraliss 10"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, message.get_args(), MagicMock())
        self.assertEqual(error, f"I'm sorry, I didn't understand the dungeon `of Sethraliss`. "
                                f"Try `!help dungeons` for help with dungeon names.")

    def test_backticks_invalid_dungeon(self):
        user_input = "/addkey Moo `Fake Dungeon`` 10"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, message.get_args(), MagicMock())
        self.assertEqual(error, f"I'm sorry, I didn't understand the dungeon `Fake Dungeon`. "
                                f"Try `!help dungeons` for help with dungeon names.")

    def test_backticks_invalid_level(self):
        user_input = "/addkey Moo Temple of Sethraliss `Bad`Level`"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, message.get_args(), MagicMock())
        self.assertEqual(error, f"`BadLevel` isn't a valid dungeon level; please input a number.")
