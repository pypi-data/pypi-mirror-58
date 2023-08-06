import json
from datetime import datetime, timedelta


class env_type:
    def __init__(self, config_id, web_endpoint, api_endpoint):
        self.config_id = config_id
        self.web_endpoint = web_endpoint
        self.api_endpoint = api_endpoint


class environment:
    PRODUCTION = env_type('api.ebay.com', 'https://auth.ebay.com/oauth2/authorize',
                          'https://api.ebay.com/identity/v1/oauth2/token')
    SANDBOX = env_type('api.sandbox.ebay.com', 'https://auth.sandbox.ebay.com/oauth2/authorize',
                       'https://api.sandbox.ebay.com/identity/v1/oauth2/token')


class credentials:
    def __init__(self, client_id, client_secret, dev_id, ru_name):
        self.client_id = client_id
        self.dev_id = dev_id
        self.client_secret = client_secret
        self.ru_name = ru_name


class oAuth_token:
    def __init__(self, error=None, access_token=None, refresh_token=None,
                 token_expiry=None, refresh_token_expiry=None,
                 expires_in=None, refresh_token_expires_in=None, **kwargs):
        """
        token_expiry: datetime in UTC
        refresh_token_expiry: datetime in UTC
        """
        self.error = error

        self.access_token = access_token
        self.refresh_token = refresh_token

        if (not token_expiry) and expires_in:
            token_expiry = datetime.utcnow() + timedelta(
                seconds=int(expires_in)) - timedelta(minutes=5)
        self.token_expiry = token_expiry

        if (not refresh_token_expiry) and refresh_token_expires_in:
            refresh_token_expiry = datetime.utcnow() + timedelta(
                seconds=int(refresh_token_expires_in)) - timedelta(minutes=5)
        self.refresh_token_expiry = refresh_token_expiry

        self.__token_dict = None

    def __str__(self):
        return json.dumps(self.token_dict)

    @property
    def token_dict(self):
        if self.__token_dict is None:
            self.__token_dict = self.to_dict()
        return self.__token_dict

    def to_dict(self):
        token_dict = dict()
        if self.error is not None:
            token_dict['error'] = self.error
        else:
            if self.access_token:
                token_dict.update({
                    'access_token': self.access_token,
                    'access_token_expiry': self.token_expiry
                })
            if self.refresh_token:
                token_dict.update({
                    'refresh_token': self.refresh_token,
                    'refresh_token_expiry': self.refresh_token_expiry,
                })
        return token_dict
