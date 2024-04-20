import requests

from .version import __version__
from requests.exceptions import HTTPError


class Client(object):
    """Client"""
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.url = 'https://api.buttercms.com/v3/'

    def api_get(self, slug='', params=None, path_override=None):
        payload = {
            'auth_token': self.auth_token,
        }
        if params:
            payload.update(params)

        headers = {
            'X-Butter-Client': 'Python/{}'.format(__version__),
            'Accept-Encoding': 'gzip',
        }

        if path_override:
            path = path_override
        else:
            path = self.path

        try:
            response = requests.get(
                url=self.url + path + str(slug),
                params=payload,
                headers=headers,
                timeout=10,
            )
        except requests.exceptions.Timeout:
            raise

        # We are not using response.raise_for_status(), as it only raises errors for definite error codes; we want to raise errors for any status other than 200.  
        # more info here: https://github.com/ButterCMS/buttercms-python/issues/5
        if response.status_code != 200: 
            raise HTTPError(response.status_code)

        return response.json()

    def get(self, slug='', params=None):
        return self.api_get(slug=slug, params=params)
