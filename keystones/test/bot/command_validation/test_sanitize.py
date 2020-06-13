import unittest

from keystones.bot.command_validation import sanitize


class TestSanitize(unittest.TestCase):
    def test_remove_backticks(self):
        user_input = 'Trololo `lo` lol'
        output = sanitize(user_input)
        self.assertEqual(output, 'Trololo lo lol')

    def test_remove_linebreaks(self):
        user_input = 'Tralala \nla\n la'
        output = sanitize(user_input)
        self.assertEqual(output, 'Tralala la la')

    def test_remove_backticks_and_linebreaks(self):
        user_input = 'Tralala \nla `la`'
        output = sanitize(user_input)
        self.assertEqual(output, 'Tralala la la')

    def test_normal(self):
        user_input = 'Normal text'
        output = sanitize(user_input)
        self.assertEqual(output, 'Normal text')
