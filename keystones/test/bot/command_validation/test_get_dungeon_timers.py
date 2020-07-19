import unittest
from unittest.mock import Mock, patch

from keystones.bot.command_validation import get_dungeon_timers


class TestGetDungeonTimers(unittest.TestCase):
    def test_no_name(self):
        res = get_dungeon_timers()
        self.assertEqual(res, 'You must enter a dungeon name. Try `!dungeons` to see dungeon names.')

    def test_invalid_name(self):
        res = get_dungeon_timers('foo')
        self.assertEqual(res, 'I\'m sorry, I didn\'t understand the dungeon `foo`. '
                              'Try `!dungeons` to see dungeon names.')

    @patch('keystones.external.blizzard_api.BlizzardAPI.get_dungeon_timers',
           Mock(return_value={1: 600000, 2: 750000, 3: 900000}))  # 10 mins, 12.5 mins, 15 mins
    def test_valid_name(self):
        res = get_dungeon_timers('Waycrest', 'Manor')
        self.assertEqual(res, 'Waycrest Manor timers:\n'
                              '+1: 10:00\n'
                              '+2: 12:30\n'
                              '+3: 15:00')

    @patch('keystones.external.blizzard_api.BlizzardAPI.get_dungeon_timers',
           Mock(return_value={1: 600000, 2: 750000, 3: 900000}))  # 10 mins, 12.5 mins, 15 mins
    def test_valid_nickname(self):
        res = get_dungeon_timers('wcm')
        self.assertEqual(res, 'Waycrest Manor timers:\n'
                              '+1: 10:00\n'
                              '+2: 12:30\n'
                              '+3: 15:00')


if __name__ == '__main__':
    unittest.main()
