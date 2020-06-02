import time
from secrets import BLIZZARD_CLIENT_ID, BLIZZARD_CLIENT_SECRET

from keystones.core.oauth import OAuth


BLIZZARD_API_TOKEN_URL = 'https://us.battle.net/oauth/token'

# A wrapper class that makes accessing the Blizzard api easy.
# Uses a singleton to be easier to use between commands.
# Should only be accessed via `get_instance()` instead
# of calling the constructor directly.
class BlizzardAPI(OAuth):
    __instance = None

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
        if not self._current_period or current_timestamp > self.current_period_end_timestamp:
            self._update_current_period()
        return self._current_period

    def _update_current_period(self):
        data = self.get('https://us.api.blizzard.com/data/wow/mythic-keystone/period/index?namespace=dynamic-us&locale=en_US')
        self._current_period = data['current_period']['id']

    @property
    def current_period_end_timestamp(self):
        if not self._current_period_end_timestamp:
            self._update_current_period_end_timestamp()
        return self._current_period_end_timestamp

    def _update_current_period_end_timestamp(self):
        data = self.get(f'https://us.api.blizzard.com/data/wow/mythic-keystone/period/{self.current_period}?namespace=dynamic-us&locale=en_US')
        self._current_period_end_timestamp = data['end_timestamp']
