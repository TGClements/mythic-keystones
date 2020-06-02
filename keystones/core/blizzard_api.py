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

    def get_dungeons(self):
        data = self.get('https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/index?namespace=dynamic-us&locale=en_US')
        return data

    def get_current_period(self):
        data = self.get('https://us.api.blizzard.com/data/wow/mythic-keystone/period/index?namespace=dynamic-us&locale=en_US')
        self.current_period = data.current_period
        return data.current_period

    def get_current_period_end_timestamp(self):
        if not self.current_period:
            self.get_current_period()
        data = self.get(f'https://us.api.blizzard.com/data/wow/mythic-keystone/period/{self.current_period}?namespace=dynamic-us&locale=en_US')
        self.current_period_end_timestamp = data.end_timestamp
        return data.end_timestamp
