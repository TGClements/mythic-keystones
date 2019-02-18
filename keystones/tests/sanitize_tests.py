import unittest

from keystones.core.command_validation import sanitize


class SanitizeTests(unittest.TestCase):
    def test_remove_backticks(self):
        user_input = "Trololo `lo` lol"
        output = sanitize(user_input)
        self.assertEqual(output, "Trololo lo lol")

    def test_remove_linebreaks(self):
        user_input = "Tralala \nla\n la"
        output = sanitize(user_input)
        self.assertEqual(output, "Tralala la la")
