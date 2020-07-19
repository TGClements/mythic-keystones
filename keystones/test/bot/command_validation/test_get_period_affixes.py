import unittest
from unittest.mock import patch, PropertyMock

from keystones.bot.command_validation import get_period_affixes


class TestGetPeriodAffixes(unittest.TestCase):
    def test_non_numeric_offset(self):
        res = get_period_affixes('foo')
        self.assertEqual(res, 'The offset must be an integer between 0 and 11 (inclusive).')

    def test_past_offset(self):
        res = get_period_affixes(-1)
        self.assertEqual(res, 'Cannot get past affixes.')

    def test_large_offset(self):
        res = get_period_affixes(12)
        self.assertEqual(res, 'Cannot get affixes more than 11 weeks into the future.')

    @patch('keystones.external.blizzard_api.BlizzardAPI.current_period', PropertyMock(return_value=1))
    @patch('keystones.external.blizzard_api.BlizzardAPI.current_seasonal_affix', PropertyMock(return_value=117))
    def test_valid_offset(self):
        # Mock seasonal affix to prevent needing to update tests every season
        res = get_period_affixes(5)
        self.assertEqual(res, 'Fortified, Bursting, Volcanic, Reaping')

    @patch('keystones.external.blizzard_api.BlizzardAPI.current_period', PropertyMock(return_value=1))
    @patch('keystones.external.blizzard_api.BlizzardAPI.current_seasonal_affix', PropertyMock(return_value=117))
    def test_numeric_offset_as_string(self):
        # Mock seasonal affix to prevent needing to update tests every season
        res = get_period_affixes('5')
        self.assertEqual(res, 'Fortified, Bursting, Volcanic, Reaping')


if __name__ == '__main__':
    unittest.main()
