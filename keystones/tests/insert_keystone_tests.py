import unittest
from unittest.mock import MagicMock

from keystones.tests.discord_mocks import DiscordMessage, DiscordCtx

from keystones.core.command_validation import insert_keystone

from keystones.db.database_manager import DatabaseManager


class InsertKeystoneTests(unittest.TestCase):
    def setUp(self):
        self.db_manager = DatabaseManager()
        self.db_manager.add_keystone = MagicMock(return_value=True)

    def test_insert_invalid_dungeon(self):
        user_input = "!add Moo dsjdaijdsa 10"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, self.db_manager, *message.get_args())
        self.assertEqual(error, f"I'm sorry, I didn't understand the dungeon "
                                f"`dsjdaijdsa`. Try `!dungeons` to see dungeon"
                                f" names.")

    def test_insert_invalid_level(self):
        user_input = "!add Moo Waycrest NaN"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, self.db_manager, *message.get_args())
        self.assertEqual(error, f"`NaN` isn't a valid dungeon level.")

    def test_invalid_num_args(self):
        user_input = "!add Moo Too"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, self.db_manager, *message.get_args())
        self.assertEqual(error, "I'm sorry, I didn't understand that. Try "
                                "`!help add` for help with formatting.")

    def test_valid_insertion(self):
        user_input = "!add Moo Waycrest 10"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, self.db_manager, *message.get_args())
        self.assertEqual(error, 'Added Waycrest Manor +10 for Moo')

    def test_valid_insertion_with_spaces(self):
        user_input = "!add Moo Waycrest Manor 10"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, self.db_manager, *message.get_args())
        self.assertEqual(error, 'Added Waycrest Manor +10 for Moo')

    def test_valid_insertion_plus_level(self):
        user_input = "!add Moo Waycrest Manor +10"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, self.db_manager, *message.get_args())
        self.assertEqual(error, 'Added Waycrest Manor +10 for Moo')

    def test_no_character_name(self):
        user_input = "!add Temple of Sethraliss 10"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, self.db_manager, *message.get_args())
        self.assertEqual(error, f"I'm sorry, I didn't understand the dungeon "
                                f"`of Sethraliss`. Try `!dungeons` to see "
                                f"dungeon names.")

    def test_backticks_invalid_dungeon(self):
        user_input = "!add Moo `Fake Dungeon`` 10"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, self.db_manager, *message.get_args())
        self.assertEqual(error, f"I'm sorry, I didn't understand the dungeon "
                                f"`Fake Dungeon`. Try `!dungeons` to see "
                                f"dungeon names.")

    def test_backticks_invalid_level(self):
        user_input = "!add Moo Temple of Sethraliss `Bad`Level`"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, self.db_manager, *message.get_args())
        self.assertEqual(error, f"`BadLevel` isn't a valid dungeon level.")

    def test_invalid_character_name(self):
        user_input = "!add Moo's tos 5"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, self.db_manager, *message.get_args())
        self.assertEqual(error, f"Character names can only contain letters, "
                                f"numbers, underscores, and dashes.")

    def test_valid_character_name_all(self):
        user_input = "!add M_5-m wm 5"
        message = DiscordMessage(user_input)
        ctx = DiscordCtx(message)
        error = insert_keystone(ctx, self.db_manager, *message.get_args())
        self.assertEqual(error, f"Added Waycrest Manor +5 for M_5-m")
