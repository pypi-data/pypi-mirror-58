import base64
import json
import logging
import os
import urllib

import requests

from .model import oAuth_token


LOGFILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'eBay_Oauth_log.txt'
)


logging.basicConfig(
    level=logging.DEBUG,
    filename=LOGFILE,
    format="%(asctime)s: %(levelname)s - %(funcName)s: %(message)s",
    filemode='w'
)


class EbayOAuthClientError(Exception):
    pass


class EbayOAuthClient:
    
    def __init__(self, env_type, credentials, logger=None, **kwargs):
        self.env_type = env_type
        self.credentials = credentials
        self.headers = self._generate_request_headers(self.credentials)
        self.logger = logger or logging

    @staticmethod
    def _generate_request_headers(credentials):
        b64_string = f'{credentials.client_id}:{credentials.client_secret}'.encode()
        b64_encoded_credential = base64.b64encode(b64_string).decode("utf-8")
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {b64_encoded_credential}',
        }
        return headers

    def generate_user_authorization_url(self, scopes: list, state: str = None):
        """
        env_type = environment.SANDBOX or environment.PRODUCTION
        scopes = list of strings
        """
        param = {
            'client_id': self.credentials.client_id,
            'redirect_uri': self.credentials.ru_name,
            'response_type': 'code',
            'prompt': 'login',
            'scope': ' '.join(scopes)
        }

        if state is not None:
            param.update({'state': state})

        query = urllib.parse.urlencode(param)
        return f"{self.env_type.web_endpoint}?{query}"

    def _get_token(self, data):
        response = requests.post(self.env_type.api_endpoint, data=data, headers=self.headers)
        content = json.loads(response.content)

        status = response.status_code
        if status != requests.codes.ok:
            message = (
                f"Unable to retrieve token.  Status code: {status} - {requests.status_codes._codes[status]}\n"
                f"Error: {content['error']} - {content['error_description']}"
            )
            self.logger.error(message)
            raise EbayOAuthClientError(message)

        return oAuth_token(**content)

    def get_application_access_token(self, scopes):
        self.logger.info("Trying to get a new application access token ... ")
        body = {
            'grant_type': 'client_credentials',
            'redirect_uri': self.credentials.ru_name,
            'scope': ' '.join(scopes),
        }
        return self._get_token(data=body)

    def exchange_code_for_access_token(self, code):
        self.logger.info("Trying to get a new user access token ... ")
        body = {
            'grant_type': 'authorization_code',
            'redirect_uri': self.credentials.ru_name,
            'code': code,
        }
        return self._get_token(data=body)

    def get_user_access_token(self, refresh_token, scopes):
        self.logger.info("Trying to get a new user access token ... ")
        if refresh_token is None:
            raise AttributeError("credential object does not contain refresh_token and/or scopes")
        body = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'scope': ' '.join(scopes),
        }
        return self._get_token(data=body)
