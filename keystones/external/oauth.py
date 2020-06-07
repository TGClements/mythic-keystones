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
                resp.raise_for_status()
            return resp.json()
