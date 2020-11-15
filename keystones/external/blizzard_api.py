import time
from secrets import BLIZZARD_CLIENT_ID, BLIZZARD_CLIENT_SECRET

from keystones.external.oauth import OAuth


BLIZZARD_API_TOKEN_URL = 'https://us.battle.net/oauth/token'


# A wrapper class that makes accessing the Blizzard api easy.
# Uses a singleton to be easier to use between commands.
# Should only be accessed via `get_instance()` instead
# of calling the constructor directly.
class BlizzardAPI(OAuth):
    __instance = None

    api_base_url = 'https://us.api.blizzard.com/data/wow/'

    # Affixes are on a set rotation, but it's not directly available
    # through the API so we need to hardcode the rotation.
    affix_rotation = [
        [10, 8, 12],
        [9, 5, 3],
        [10, 7, 2],
        [9, 11, 4],
        [10, 8, 14],
        [9, 7, 13],
        [10, 11, 3],
        [9, 6, 4],
        [10, 5, 14],
        [9, 11, 2],
        [10, 7, 12],
        [9, 6, 13],
    ]

    # The seasonal affix is also not available through the api
    # so we need to manually set it as well
    current_seasonal_affix = 121

    @staticmethod
    def get_instance():
        if not BlizzardAPI.__instance:
            BlizzardAPI()
        return BlizzardAPI.__instance

    def __init__(self):
        if BlizzardAPI.__instance:
            raise Exception('There is already an active BlizzardAPI instance')

        OAuth.__init__(self, BLIZZARD_CLIENT_ID, BLIZZARD_CLIENT_SECRET, BLIZZARD_API_TOKEN_URL)
        BlizzardAPI.__instance = self

        # Don't call the api unless we actually need to
        self._current_period = None
        self._current_period_end_timestamp = None

    @property
    def current_period(self):
        current_timestamp = time.time() * 1000
        if (not self._current_period) or current_timestamp > self._current_period_end_timestamp:
            self._update_current_period()
        return self._current_period

    def _update_current_period(self):
        # The current period and current period end timestamp are closely related so fetch them together
        period_data = self.get(f'{BlizzardAPI.api_base_url}mythic-keystone/period/index?namespace=dynamic-us&locale=en_US')
        self._current_period = period_data['current_period']['id']

        time_data = self.get(f'{BlizzardAPI.api_base_url}mythic-keystone/period/{self._current_period}?namespace=dynamic-us&locale=en_US')
        self._current_period_end_timestamp = time_data['end_timestamp']

    @property
    def current_period_end_timestamp(self):
        current_timestamp = time.time() * 1000
        if (not self._current_period_end_timestamp) or current_timestamp > self._current_period_end_timestamp:
            self._update_current_period()
        return self._current_period_end_timestamp

    @staticmethod
    def get_affixes_for_timeperiod(timeperiod):
        return BlizzardAPI.affix_rotation[timeperiod % len(BlizzardAPI.affix_rotation)] + [BlizzardAPI.current_seasonal_affix]

    def get_affix_details(self, affix_id):
        data = self.get(f'{BlizzardAPI.api_base_url}keystone-affix/{affix_id}?namespace=static-us&locale=en_US')
        return data['name'], data['description']

    def get_dungeon_timers(self, dungeon_id):
        data = self.get(f'{BlizzardAPI.api_base_url}mythic-keystone/dungeon/{dungeon_id}?namespace=dynamic-us&locale=en_US')
        upgrade_levels = {entry['upgrade_level']: entry['qualifying_duration']
                          for entry in data['keystone_upgrades']}
        return upgrade_levels
