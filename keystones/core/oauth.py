from secrets import BLIZZARD_CLIENT_ID, BLIZZARD_CLIENT_SECRET

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from oauthlib.oauth2 import TokenExpiredError


class OAuth():
    def __init__(self, client_id, client_secret, token_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url

        client = self.client = BackendApplicationClient(client_id=client_id)
        self.oauth = OAuth2Session(client=client)
        self.fetch_token()

    def fetch_token(self):
        token = self.token = self.oauth.fetch_token(token_url=self.token_url,
            client_id=self.client_id, client_secret=self.client_secret)
        return self.token

    def get(self, url):
        try:
            resp = self.oauth.get(url)
        except TokenExpiredError as e:
            self.fetch_token()
            resp = self.oauth.get(url)
        finally:
            if resp.status_code != 200:
                raise Exception(resp.status_code)
            return resp.json()

class BlizzardAPI(OAuth):
    def __init__(self):
        BLIZZARD_API_TOKEN_URL = 'https://us.battle.net/oauth/token'
        OAuth.__init__(self, BLIZZARD_CLIENT_ID, BLIZZARD_CLIENT_SECRET, BLIZZARD_API_TOKEN_URL)

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
